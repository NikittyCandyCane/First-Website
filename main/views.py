from django.shortcuts import render, HttpResponse

# Create your views here.


def index(response, id):
    return HttpResponse('<h1>%s</h1>' % id)

def home(request):
    return render(request,"home.html")