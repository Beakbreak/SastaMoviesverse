from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('insert/', views.insert),
    path('delete/',views.delete_all),
    path('ratings/<str:pk>/', views.Ratings.as_view()),
    path('create_userid/<str:pk>/',views.create_userid),
    path('train/<str:pk>/',views.train.as_view()),
    path('suggestions/<str:pk>/',views.suggestions.as_view()),
    path('genre/<str:pk>/', views.genre.as_view()),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ratings/', views.RatingCreateView.as_view(), name='rating-create'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('get_id/', views.Userid.as_view()),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('increment/<str:pk>/', views.update_number.as_view()),
    path('trending/',views.Trending.as_view()),
    path('highly_rated',views.Highly_rated.as_view()),
]