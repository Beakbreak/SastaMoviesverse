from django.urls import path
from ..recommender_system import views

urlpatterns = [
    path('',views.getRoutes)
]
