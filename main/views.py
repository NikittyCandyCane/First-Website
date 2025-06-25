from django.shortcuts import render, redirect
import random
from django.http import HttpResponse

#HttpReponse : Wraps it in a response package that Django can send to the server
#Render: First uses Django logic to fill in variables and do logic, and then also wraps it in a response package

def home(request):
    nickname = random.choice(['cutie pie', 'poopoo', 'sprinkle tart', 'peepee', 'wonderous rainbow', 'confetti bomb', 'hottie hottie shawtie'])
    if request.method == 'POST':
        question = request.POST['question']
        if 'bad' in question or 'eh' in question or 'dont like' in question or 'don\'t like' in question or 'not good' in question or 'not great' in question or 'terrible' in question or 'not cool' in question or 'dont really like' in question or 'don\'t really like' in question:
            isgood = False
        elif 'good' in question or 'great' in question or 'awesome' in question or 'cool' in question or 'like' in question or 'love' in question or 'ok' in question or 'okay' in question:
            isgood = True
        else:
            isgood = 'did not understand'
        return render(request, 'main/home.html', context = {'nickname' : nickname, 'isgood' : isgood})

    return render(request, 'main/home.html', context = {'nickname' : nickname, 'isgood': 'n/a'})

def me(request):
    return render(request, 'main/me.html', {})

def catpics(request):
    return render(request, 'main/catpics.html', {})