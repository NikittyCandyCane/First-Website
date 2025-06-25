from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('me/', views.me),
    path('catpics/', views.catpics),
    path('maze/', views.maze),
    path('maze/deadend', views.maze_deadend),
    path('maze/straight', views.maze_straight)
]