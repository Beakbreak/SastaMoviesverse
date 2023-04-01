from rest_framework import serializers
from collaborative.models import Movie, Rating, Suggestion, userid
from django.contrib.auth.models import User

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = '__all__'
        
class useridSerializer(serializers.ModelSerializer):
    class Meta:
        model= userid
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']