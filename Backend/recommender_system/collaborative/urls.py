from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('insert/', views.insert),
    path('delete/', views.delete_all),
    path('ratings/<str:pk>/', views.get_ratings),
    path('trial/<str:pk>/',views.trial),
    path('train/<str:pk>/',views.train),
    path('suggestions/',views.create_suggestions)
]