from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(response):
    return HttpResponse('hello world')