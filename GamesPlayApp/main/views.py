from django.shortcuts import render, redirect

from GamesPlayApp.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateGameForm, EditGameForm, \
    DeleteGameForm
from GamesPlayApp.main.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def index(request):
    return render(request, 'home-page.html')


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == "POST":
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = CreateGameForm()

    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)


def show_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    game_count = len(games)
    average_game_rating = 0
    if games:
        average_game_rating = sum(x.rating for x in games)/game_count
    context = {
        'profile': profile,
        'games': games,
        'game_count': game_count,
        'average_game_rating': average_game_rating,
    }

    return render(request, 'details-profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


