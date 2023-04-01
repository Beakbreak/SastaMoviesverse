from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('insert/', views.create_suggestions),
    path('delete/', views.delete_all.as_view()),
    path('ratings/<str:pk>/', views.Ratings.as_view()),
    path('trial/',views.trial),
    path('train/<str:pk>/',views.train.as_view()),
    path('suggestions/<str:pk>/',views.suggestions.as_view()),
    path('genre/<str:pk>/', views.genre.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',views.UserSerializer),
    path('ratings/', views.RatingCreateView.as_view(), name='rating-create'),
]