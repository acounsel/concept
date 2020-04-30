from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Phrase(models.Model):

    name = models.CharField(max_length=200, unique=True)
    difficulty_level = models.IntegerField(default=1)
    category = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Concept(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    icon = models.FileField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class Token(models.Model):

    COLOR_CHOICES = (
        ('green', 'Green'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
    )
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='green')
    concept = models.ForeignKey(Concept, 
        on_delete=models.SET_NULL, blank=True, null=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        if self.is_primary:
            return 'Primary ' + self.color
        else:
            return self.color + ' cube'

class Game(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game-detail', 
            kwargs={'pk':self.id})

    def get_next_round_number(self):
        num_rounds = Round.objects.filter(game=self).count()
        return num_rounds + 1

class Player(models.Model):

    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Round(models.Model):

    game = models.ForeignKey(Game, 
        on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    phrase = models.ForeignKey(Phrase, 
        on_delete=models.SET_NULL, 
        blank=True, null=True)
    active_player = models.ForeignKey(Player, 
        on_delete=models.CASCADE)
    guessing_players = models.ManyToManyField(
        Player, blank=True, related_name='guessers')

    def __str__(self):
        return self.game.name+' Round '+self.number



