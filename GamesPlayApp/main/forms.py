from django.forms import ModelForm, forms
from django import forms

from GamesPlayApp.main.models import Profile, Game


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')


class DeleteProfileForm(ModelForm):
    def save(self, commit=True):
        games = Game.objects.all()
        self.instance.delete()
        games.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'image': 'Image URL'
        }


class EditGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'image': 'Image URL'
        }


class DeleteGameForm(ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = ()
