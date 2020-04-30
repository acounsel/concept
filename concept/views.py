from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Concept, Phrase, Token, Game, Player, Round

# Home page, shows concepts and phrases
def home(request):
    context = {
        'first_name': 'Samer',
        'last_name': 'Araabi',
        'concepts': Concept.objects.all(),
        'phrase_list': Phrase.objects.all(),
    }
    return render(request, 'home.html', context)

class GameMixin:

    def get_context_data(self):
        context = super().get_context_data()
        game_id = self.kwargs['game_id']
        game = Game.objects.get(id=game_id)
        context['game'] = game
        return context

class TokenList(GameMixin, ListView):
    model = Token

    def get_context_data(self):
        context = super().get_context_data()
        game_round = Round.objects.get(
            id=self.kwargs['round_id'])
        phrase = Phrase.objects.get(
            id=self.kwargs['phrase_id'])
        game_round.phrase = phrase
        game_round.save()
        context['round'] = game_round
        context['phrase'] = phrase
        return context

class TokenDetail(DetailView):
    model = Token

class CreateToken(CreateView):
    model = Token
    fields = ('color', 'is_primary')
    success_url = '/tokens/'

class UpdateToken(UpdateView):
    model = Token
    fields = ('concept',)

    def get_success_url(self):
        return reverse_lazy('token-list',
            kwargs={
            'game_id':self.kwargs['game_id'],
            'round_id':self.kwargs['round_id'],
            'phrase_id': self.kwargs['phrase_id'],
        })

class PhraseList(GameMixin, ListView):
    model = Phrase

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('?')[:5]

    def get_context_data(self):
        context['round'] = Round.objects.get(
            id=self.kwargs['round_id'])
        return context

class GameCreate(CreateView):
    model = Game
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy('round-create',
            kwargs={'game_id':self.object.id})

class GameDetail(DetailView):
    model = Game

class RoundCreate(CreateView):
    model = Round
    fields = ('game', 'number', 'active_player')

    def get_success_url(self):
        return reverse_lazy('phrase-list', 
            kwargs={
                'round_id': self.object.id,
                'game_id': self.object.game.id,
            })

