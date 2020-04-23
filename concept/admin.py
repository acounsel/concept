from django.contrib import admin

from .models import Phrase, Concept, Token, Game, Player, Round

admin.site.register(Phrase)
admin.site.register(Concept)
admin.site.register(Token)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Round)
