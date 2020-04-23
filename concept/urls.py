from django.urls import include, path

from .views import home, CreateToken, TokenList, UpdateToken

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
]