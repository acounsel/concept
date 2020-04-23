from django.urls import include, path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tokens/', TokenList.as_view(), 
        name='token-list'),
    path('tokens/create/', 
        CreateToken.as_view(), 
        name='create-token'),
    path('tokens/<pk>/update/', 
        UpdateToken.as_view(), 
        name='update-token'),
    path('phrases/', PhraseList.as_view(),
        name='phrase-list'),
    path('game/create/', GameCreate.as_view(), 
        name='game-create'),
    path('game/<pk>/', GameDetail.as_view(), 
        name='game-detail'),
]