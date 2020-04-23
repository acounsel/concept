from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Concept, Phrase, Token

# Home page, shows concepts and phrases
def home(request):
    context = {
        'first_name': 'Samer',
        'last_name': 'Araabi',
        'concepts': Concept.objects.all(),
        'phrase_list': Phrase.objects.all(),
    }
    return render(request, 'home.html', context)

class TokenList(ListView):
    model = Token

class TokenDetail(DetailView):
    model = Token

class CreateToken(CreateView):
    model = Token
    fields = ('color', 'is_primary')
    success_url = ('/tokens/')

class UpdateToken(UpdateView):
    model = Token
    fields = ('concept',)
    success_url = ('/tokens/')
