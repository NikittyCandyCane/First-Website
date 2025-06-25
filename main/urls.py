from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('me/', views.me),
    path('catpics/', views.catpics),
    path('maze/', views.maze),
    path('maze/deadend', views.maze_deadend),
    path('maze/straight/straight/right/right', views.maze_straight_straight_right_right),
    path('maze/straight', views.maze_straight),
    path('maze/straight/straight', views.maze_straight_straight),
    path('maze/straight/straight/right', views.maze_straight_straight_right),
    path('maze/straight/straight/right/straight', views.maze_straight_straight_right_straight),
    path('maze/straight/straight/right/straight/left', views.maze_straight_straight_right_straight_left),
    path('maze/straight/straight/right/straight/left/left', views.maze_straight_straight_right_straight_left_left),
]