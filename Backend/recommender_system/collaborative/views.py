from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from collaborative.models import Movie, Rating, Suggestion
from .serializers import RatingSerializer, MovieSerializer
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
from .training_fuctions import cofi_cost_func_v
from django.forms import model_to_dict


@api_view (['GET'])
def get_ratings(request, pk):
    ratings=Rating.objects.filter(userId=pk)
    ratings_Dict=[ model_to_dict(rating) for rating in ratings]
    print(ratings_Dict[0])
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
        
    

@api_view (['GET'])
def train(request, pk):
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
    print(ratings_Dict)
    for i in ratings_Dict:
        ori_id= i['movieId']
        movie_obj=Movie.objects.get(movieId=ori_id)
        serializer_m = MovieSerializer(movie_obj, many=False)
        movie_Dict = model_to_dict(movie_obj)
        print(movie_Dict)
        movie=int(movie_Dict['id'])
        print(movie)
        rating=i['rating']
        print(rating)
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

@api_view (['GET'])
def create_suggestions(request):
    df=pd.read_csv('suggestions.csv',index_col=[0])
    #print(df)
    row_iter = df.iterrows()
    objs = [
        Suggestion(
            userId = index,
            suggestion_1  = row['suggestion_1'],
            suggestion_2  = row['suggestion_2'],
            suggestion_3  = row['suggestion_3'],
            suggestion_4  = row['suggestion_4'],
            suggestion_5  = row['suggestion_5'],
            suggestion_6  = row['suggestion_6'],
            suggestion_7  = row['suggestion_7'],
            suggestion_8  = row['suggestion_8'],
            suggestion_9  = row['suggestion_9'],
            suggestion_10  = row['suggestion_10'],
            suggestion_11 = row['suggestion_11'],
            suggestion_12 = row['suggestion_12'],
            suggestion_13 = row['suggestion_13'],
            suggestion_14 = row['suggestion_14'],
            suggestion_15 = row['suggestion_15']
        )

        for index, row in row_iter
    ]
    Suggestion.objects.bulk_create(objs)
    return Response('ok')

@api_view (['GET'])
def delete_all(request):
    Suggestion.objects.all().delete()
    return Response('ok')