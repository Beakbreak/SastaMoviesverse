from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from collaborative.models import Movie, Rating
from .serializers import RatingSerializer, MovieSerializer
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from .training_fuctions import cofi_cost_func_v
from django.forms import model_to_dict
from django_pandas.io import read_frame


@api_view (['GET'])
def get_ratings(request, pk):
    ratings=Rating.objects.filter(userId=pk)
    ratings_Dict=[ model_to_dict(rating) for rating in ratings]
    print(ratings_Dict)
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

# @api_view (['GET'])
# def get_suggestions(request,pk)-

@api_view(['GET'])
def trial(request, pk):
    movie_obj=Movie.objects.get(movieId=209139)
    movie_Dict = model_to_dict(movie_obj)
    print(movie_Dict)
    serializer = MovieSerializer(movie_obj, many=False)
    return Response(serializer.data)   
        
    

# @api_view (['GET'])
# def train(request, pk):
#     df_R = pd.read_pickle('R.pkl')
#     R=df_R.to_numpy()
#     df_Y = pd.read_pickle('Y.pkl')
#     Y=df_Y.to_numpy()
#     df_X = pd.read_pickle('X.pkl')
#     X=df_X.to_numpy()
#     df_W = pd.read_pickle('W.pkl')
#     W=df_W.to_numpy()
#     df_b = pd.read_pickle('b.pkl')
#     b=df_b.to_numpy()
#     num_movies, num_features = X.shape
#     num_users,_ = W.shape-
#     my_ratings = np.zeros(num_movies)
#     for i in range(len(df.index.to_list())):
#         ori_id=df.iloc[i]['movieId']
#         id_list=df_m.index.to_list()
#         movie=id_list[0]
#         rating=df.iloc[i]['rating']
#         my_ratings[movie]= rating    
    
