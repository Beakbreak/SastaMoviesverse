from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from collaborative.models import Movie, Rating, Suggestion
from .serializers import RatingSerializer, MovieSerializer, SuggestionSerializer
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from .training_fuctions import cofi_cost_func_v
from django.forms import model_to_dict
from django.db.models import Case, When
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from .paginations import CustomNumberPagination


class delete_all(APIView):
    def get(self, request):
        Movie.objects.all().delete()
        return Response('ok')


class Ratings(APIView):  
    def get(request, pk):
        ratings=Rating.objects.filter(userId=pk)
        ratings_Dict=[ model_to_dict(rating) for rating in ratings]
        print(ratings_Dict[0])
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

# @api_view (['GET'])
# def get_suggestions(request,pk)-

# def trial(request, pk):
#     movie_obj=Movie.objects.get(movieId=209139)
#     movie_Dict = model_to_dict(movie_obj)
#     print(movie_Dict)
#     serializer = MovieSerializer(movie_obj, many=False)
#     return Response(serializer.data)   
        
    

class train(APIView):
    def get(self, request, pk):
        df_R = pd.read_pickle('R.pkl')
        R=df_R.to_numpy()
        df_Y = pd.read_pickle('Y.pkl')
        Y=df_Y.to_numpy()
        df_X = pd.read_pickle('X.pkl')
        X=df_X.to_numpy()
        df_W = pd.read_pickle('W.pkl')
        W=df_W.to_numpy()
        df_b = pd.read_pickle('b.pkl')
        b=df_b.to_numpy()
        num_movies, num_features = X.shape
        num_users,_ = W.shape
        my_ratings = np.zeros(num_movies)
        ratings=Rating.objects.filter(userId=pk)
        ratings_Dict=[ model_to_dict(rating) for rating in ratings]
        # print(ratings_Dict)
        for i in ratings_Dict:
            ori_id= i['movieId']
            movie_obj=Movie.objects.get(movieId=ori_id)
            serializer_m = MovieSerializer(movie_obj, many=False)
            movie_Dict = model_to_dict(movie_obj)
            # print(movie_Dict)
            movie=int(movie_Dict['id'])
            # print(movie)
            rating=i['rating']
            # print(rating)
            my_ratings[movie]= rating 
        print('\nNew user ratings:\n')
        for i in range(len(my_ratings)):
            if my_ratings[i] > 0 :
                movie_obj=Movie.objects.get(id=i)
                movie_Dict = model_to_dict(movie_obj)
                print(f'Rated {my_ratings[i]} for {movie_Dict["title"]}')
        Y.astype(np.float16)
        R.astype(np.int8)
        Ymean = (np.sum(Y*R,axis=1)/(np.sum(R, axis=1)+1e-12)).reshape(-1,1)
        Ymean.astype(np.float16)
        Ynorm = Y - np.multiply(Ymean, R)
        Ynorm.astype(np.float16)
        num_movies, num_users = Y.shape
        num_features = 100
        W = tf.Variable(tf.random.normal((num_users,  num_features),dtype=tf.float64),  name='W')
        X = tf.Variable(tf.random.normal((num_movies, num_features),dtype=tf.float64),  name='X')
        b = tf.Variable(tf.random.normal((1,          num_users),   dtype=tf.float64),  name='b')
        optimizer = keras.optimizers.Adam(learning_rate=1e-1)
        iterations = 200
        lambda_ = 1
        for iter in range(iterations):
            with tf.GradientTape() as tape:
                cost_value = cofi_cost_func_v(X, W, b, Ynorm, R, lambda_)
                grads = tape.gradient( cost_value, [X,W,b] )
                optimizer.apply_gradients( zip(grads, [X,W,b]) )
            if iter % 20 == 0:
                print(f"Training loss at iteration {iter}: {cost_value:0.1f}")
        p = np.matmul(X.numpy(), np.transpose(W.numpy())) + b.numpy()
        pm = p + Ymean
        my_predictions = pm[:,0]
        movies_to_send= []
        ix = tf.argsort(my_predictions, direction='DESCENDING')
        ix=ix.numpy()
        # ix=ix.to_list()
        print(ix)
        my_rated = [i for i in range(len(my_ratings)) if my_ratings[i] > 0]
        for i in range(25):
            j = ix[i]
            if j not in my_rated:
                print(j)
                movie_obj=Movie.objects.get(id=j)
                movie_Dict = model_to_dict(movie_obj)
                name=movie_Dict['title']           
                movies_to_send.append(name)
                print(name)
        for i in range(15):
            j = ix[i]
            if(i==0):
                Suggestion.objects.filter(userId=pk).update(suggestion_1=f'{j}')
            elif (i==1):
                Suggestion.objects.filter(userId=pk).update(suggestion_2=f'{j}')
            elif (i==2):
                Suggestion.objects.filter(userId=pk).update(suggestion_3=f'{j}')
            elif (i==3):
                Suggestion.objects.filter(userId=pk).update(suggestion_4=f'{j}')
            elif (i==4):
                Suggestion.objects.filter(userId=pk).update(suggestion_5=f'{j}')
            elif (i==5):
                Suggestion.objects.filter(userId=pk).update(suggestion_6=f'{j}')
            elif (i==6):
                Suggestion.objects.filter(userId=pk).update(suggestion_7=f'{j}')
            elif (i==7):
                Suggestion.objects.filter(userId=pk).update(suggestion_8=f'{j}')
            elif (i==8):
                Suggestion.objects.filter(userId=pk).update(suggestion_9=f'{j}')
            elif (i==9):
                Suggestion.objects.filter(userId=pk).update(suggestion_10=f'{j}')
            elif (i==10):
                Suggestion.objects.filter(userId=pk).update(suggestion_11=f'{j}')
            elif (i==11):
                Suggestion.objects.filter(userId=pk).update(suggestion_12=f'{j}')
            elif (i==12):
                Suggestion.objects.filter(userId=pk).update(suggestion_13=f'{j}')
            elif (i==13):
                Suggestion.objects.filter(userId=pk).update(suggestion_14=f'{j}')
            elif (i==14):
                Suggestion.objects.filter(userId=pk).update(suggestion_15=f'{j}')
        return Response('ok')

# @api_view (['GET'])
# def create_suggestions(request):
#     df=pd.read_csv('suggestions.csv',index_col=[0])
#     #print(df)
#     row_iter = df.iterrows()
#     objs = [
#         Suggestion(
#             userId = index,
#             suggestion_1  = row['suggestion_1'],
#             suggestion_2  = row['suggestion_2'],
#             suggestion_3  = row['suggestion_3'],
#             suggestion_4  = row['suggestion_4'],
#             suggestion_5  = row['suggestion_5'],
#             suggestion_6  = row['suggestion_6'],
#             suggestion_7  = row['suggestion_7'],
#             suggestion_8  = row['suggestion_8'],
#             suggestion_9  = row['suggestion_9'],
#             suggestion_10  = row['suggestion_10'],
#             suggestion_11 = row['suggestion_11'],
#             suggestion_12 = row['suggestion_12'],
#             suggestion_13 = row['suggestion_13'],
#             suggestion_14 = row['suggestion_14'],
#             suggestion_15 = row['suggestion_15']
#         )

#         for index, row in row_iter
#     ]
#     Suggestion.objects.bulk_create(objs)
#     return Response('ok')

class suggestions(APIView):
    def get_suggestions(self ,request, pk):
        suggestions=Suggestion.objects.get(userId=pk)
        suggestions_Dict=model_to_dict(suggestions)
        movieid_to_send=[]
        for i in range(15):
            movieid_to_send.append(suggestions_Dict[f'suggestion_{(i+1)}'])
        print(movieid_to_send)
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(movieid_to_send)])
        movie_suggestions = Movie.objects.filter(pk__in=movieid_to_send).order_by(preserved)
        serializer=MovieSerializer(movie_suggestions, many=True)
        return Response(serializer.data)
    
class genre(ListAPIView, CustomNumberPagination):
    pagination_class=CustomNumberPagination
    serializer_class=MovieSerializer
    def get(self, request, pk):
        if(pk=='War'):
            movies=Movie.objects.filter(War=1).order_by('number_of_ratings')
        elif (pk=='Fantasy'):
            movies=Movie.objects.filter(Fantasy=1).order_by('number_of_ratings')
        elif (pk=='Adventure'):
            movies=Movie.objects.filter(Adventure=1).order_by('number_of_ratings')
        elif (pk=='Horror'):
            movies=Movie.objects.filter(Horror=1).order_by('number_of_ratings')
        elif (pk=='Documentary'):
            movies=Movie.objects.filter(Documentary=1).order_by('number_of_ratings')
        elif (pk=='Mystery'):
            movies=Movie.objects.filter(Mystery=1).order_by('number_of_ratings')
        elif (pk=='Drama'):
            movies=Movie.objects.filter(Drama=1).order_by('number_of_ratings')    
        elif (pk=='Children'):
            movies=Movie.objects.filter(Children=1).order_by('number_of_ratings')
        elif (pk=='Romance'):
            movies=Movie.objects.filter(Romance=1).order_by('number_of_ratings')
        elif (pk=='IMAX'):
            movies=Movie.objects.filter(IMAX=1).order_by('number_of_ratings')
        elif (pk=='Comedy'):
            movies=Movie.objects.filter(Comedy=1).order_by('number_of_ratings')
        elif (pk=='Western'):
            movies=Movie.objects.filter(Western=1).order_by('number_of_ratings')
        elif (pk=='Animation'):
            movies=Movie.objects.filter(Animation=1).order_by('number_of_ratings')
        elif (pk=='Crime'):
            movies=Movie.objects.filter(Crime=1).order_by('number_of_ratings')
        elif (pk=='Musical'):
            movies=Movie.objects.filter(Musical=1).order_by('number_of_ratings')
        elif (pk=='Thriller'):
            movies=Movie.objects.filter(Thriller=1).order_by('number_of_ratings')
        elif (pk=='Sci_Fi'):
            movies=Movie.objects.filter(Sci_Fi=1).order_by('number_of_ratings')
        elif (pk=='Action'):
            movies=Movie.objects.filter(Action=1).order_by('number_of_ratings')
        elif (pk=='Film_Noir'):
            movies=Movie.objects.filter(Film_Noir=1).order_by('number_of_ratings')
        page = self.request.query_params.get('page')
        self.queryset=movies
        if page is not None:
            paginate_queryset = self.paginate_queryset(movies)
            serializer = self.serializer_class(paginate_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data)

# @api_view (['GET'])
# def insert(request):
#     df=pd.read_csv('final_movies.csv',index_col=[0])
#     #print(df)
#     row_iter = df.iterrows()
#     objs = [
#         Movie(
#             id = index,
#             mean_rating  = row['mean_rating'],
#             number_of_ratings  = row['number_of_ratings'],
#             title  = row['title'],
#             War  = row['War'],
#             Fantasy  = row['Fantasy'],
#             Adventure  = row['Adventure'],
#             Horror  = row['Horror'],
#             Documentary  = row['Documentary'],
#             Mystery  = row['Mystery'],
#             Drama  = row['Drama'],
#             Children  = row['Children'],
#             Romance  = row['Romance'],
#             IMAX  = row['IMAX'],
#             Comedy  = row['Comedy'],
#             Western  = row['Western'],
#             Animation  = row['Animation'],
#             No_genre  = row['No_genre'],
#             Crime  = row['Crime'],
#             Musical  = row['Musical'],
#             Thriller  = row['Thriller'],
# 		    Action = row['Action'],
#             Sci_Fi  = row['Sci_Fi'],
#             Film_Noir  = row['Film_Noir'],
#             movieId  = row['movieId']
#         )

#         for index, row in row_iter
#     ]
#     Movie.objects.bulk_create(objs)
#     return Response('ok')

# @api_view (['GET'])
# def trending_choices(request):