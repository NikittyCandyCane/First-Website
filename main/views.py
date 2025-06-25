from django.shortcuts import render, redirect
import random
from django.http import HttpResponse

#HttpReponse : Wraps it in a response package that Django can send to the server
#Render: First uses Django logic to fill in variables and do logic, and then also wraps it in a response package

def home(request):
    nickname = random.choice(['cutie pie', 'poopoo', 'sprinkle tart', 'peepee', 'wonderous rainbow', 'confetti bomb', 'hottie hottie shawtie', 'auraful alpha'])
    if request.method == 'POST':
        question = request.POST['question']
        if 'bad' in question or 'eh' in question or 'dont like' in question or 'don\'t like' in question or 'not good' in question or 'not great' in question or 'terrible' in question or 'not cool' in question or 'dont really like' in question or 'don\'t really like' in question:
            request.session['isgood'] = False
        elif 'good' in question or 'great' in question or 'awesome' in question or 'cool' in question or 'like' in question or 'love' in question or 'ok' in question or 'okay' in question:
            request.session['isgood'] = True
        else:
            request.session['isgood'] = 'did not understand'
        return render(request, 'main/home.html', context = {'nickname' : nickname, 'isgood' : request.session.get('isgood')})

    return render(request, 'main/home.html', context = {'nickname' : nickname, 'isgood': request.session.get('isgood')})

def me(request):
    return render(request, 'main/me.html', {})

def catpics(request):
    return render(request, 'main/catpics.html', {})

def maze(request):
    return render(request, 'main/maze.html', {})

def maze_straight(request):
    return render(request, 'main/maze_straight.html', {})

def maze_straight_straight_right(request):
    return render(reqest)

def maze_deadend(request):
    return render(request, 'main/maze_deadend.html', {})
