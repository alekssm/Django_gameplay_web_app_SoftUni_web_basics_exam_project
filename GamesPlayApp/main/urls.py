from django.urls import path

from GamesPlayApp.main.views import index, dashboard, create_game, game_details, edit_game, delete_game, create_profile, \
    show_profile, edit_profile, delete_profile

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='show dashboard'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', game_details, name='game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/details/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)
