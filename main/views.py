from django.shortcuts import render, redirect
import random
from django.http import HttpResponse

#HttpReponse : Wraps it in a response package that Django can send to the server
#Render: First uses Django logic to fill in variables and do logic, and then also wraps it in a response package

def home(request):
    nickname = random.choice(['cutie pie', 'poopoo', 'sprinkle tart', 'peepee', 'wonderous rainbow', 'confetti bomb'])
    return render(request, 'main/home.html', context = {'nickname' : nickname})