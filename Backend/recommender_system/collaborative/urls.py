from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('insert/', views.insert),
    path('delete/', views.delete_all.as_view()),
    path('ratings/<str:pk>/', views.Ratings.as_view()),
    # path('trial/<str:pk>/',views.trial),
    path('train/<str:pk>/',views.train.as_view()),
    path('suggestions/<str:pk>/',views.suggestions.as_view()),
    path('genre/<str:pk>/', views.genre.as_view())
]