from django.contrib import admin

from GamesPlayApp.main.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
