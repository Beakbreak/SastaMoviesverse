from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/')
    path('ratings/<str:pk>/', views.get_ratings),
    path('trial/<str:pk>/',views.trial)
]