from django.urls import include, path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tokens/create/', 
        CreateToken.as_view(), 
        name='create-token'),
    path('game/create/', GameCreate.as_view(), 
        name='game-create'),
    path('game/<pk>/', GameDetail.as_view(), 
        name='game-detail'),
    path('game/<int:game_id>/', include([
        path('create-round/',
            RoundCreate.as_view(),
            name='round-create'),
        path('<int:round_id>/select-phrase/', 
            PhraseList.as_view(), 
            name='phrase-list'),
        path('<int:round_id>/<int:phrase_id>/tokens/', 
            TokenList.as_view(), 
            name='token-list'),
        path('<int:round_id>/<int:phrase_id>/tokens/<pk>/update/', 
            UpdateToken.as_view(), 
            name='update-token'),
    ])),       
]