from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('me/', views.me),
    path('catpics/', views.catpics)
]