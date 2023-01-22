from flask import Flask, render_template, url_for, request
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import numpy as np
import tensorflow as tf
from tensorflow import keras
from recsys_utils import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'moviesverse'

mysql = MySQL(app)
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return "Hello world"


@app.route('/rating', methods=['POST'])
def rating_insert():
    cursor = mysql.connection.cursor()
    content = request.json

    email = content['email']
    cursor.execute(f'SELECT u_id FROM registered_users WHERE email=')

    movie_id = content['movie_id']
    rating = content['rating']

    l = cursor.fetchall()
    print(l)
    u_id = l[0][0]
    query = f"INSERT INTO new_ratings VALUES ({u_id},{movie_id},{rating})"
    data = (u_id, movie_id, rating)

    cursor.execute(query, data)
    mysql.connection.commit()


@app.route('/login', methods=['POST'])
def login():
    cursor1 = mysql.connection.cursor()

    content = request.json
    email = content['email']
    pwd = content['password']
    data = (email, pwd)
    # query = "SELECT * FROM registered_users WHERE email = %s AND password=%s"
    # cursor1.execute(query, data)

    # results = cursor1.fetchall()
    # print(results)

    query1 = "SELECT movie_id, rating FROM new_ratings WHERE u_id = (SELECT u_id FROM registered_users WHERE email = %s AND password=%s)"
    # temp = (results[0][0])

    cursor2 = mysql.connection.cursor()

    cursor2.execute(query1, data)
    # mysql.connection.commit()

    res = cursor2.fetchall()
    print(res)
    x = predict(res)
    # cursor.close()
    return x


@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = mysql.connection.cursor()
    content = request.json

    cursor.execute('SELECT * FROM registered_users')
    count = len(cursor.fetchall())
    email = content['email']
    pwd = content['password']

    query = "INSERT INTO registered_users VALUES (%s, %s, %s)"
    data = (count, email, pwd)

    cursor.execute(query, data)
    mysql.connection.commit()

    return 'ok'
    cursor.close()


def predict(res):
    print(res)
    X, W, b, num_movies, num_features, num_users = load_precalc_params_small()
    Y, R = load_ratings_small()

    print("Y", Y.shape, "R", R.shape)
    print("X", X.shape)
    print("W", W.shape)
    print("b", b.shape)
    print("num_features", num_features)
    print("num_movies",   num_movies)
    print("num_users",    num_users)
    #  From the matrix, we can compute statistics like average rating.
    tsmean = np.mean(Y[0, R[0, :].astype(bool)])
    print(f"Average rating for movie 1 : {tsmean:0.3f} / 5")
    # Reduce the data set size so that this runs faster
    num_users_r = 4
    num_movies_r = 5
    num_features_r = 3

    X_r = X[:num_movies_r, :num_features_r]
    W_r = W[:num_users_r, :num_features_r]
    b_r = b[0, :num_users_r].reshape(1, -1)
    Y_r = Y[:num_movies_r, :num_users_r]
    R_r = R[:num_movies_r, :num_users_r]

    def cofi_cost_func_v(X, W, b, Y, R, lambda_):
        """
        Returns the cost for the content-based filtering
        Vectorized for speed. Uses tensorflow operations to be compatible with custom training loop.
        Args:
        X (ndarray (num_movies,num_features)): matrix of item features
        W (ndarray (num_users,num_features)) : matrix of user parameters
        b (ndarray (1, num_users)            : vector of user parameters
        Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
        R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
        lambda_ (float): regularization parameter
        Returns:
        J (float) : Cost
        """
        j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R
        J = 0.5 * tf.reduce_sum(j**2) + (lambda_/2) * \
            (tf.reduce_sum(X**2) + tf.reduce_sum(W**2))
        return J

    # Evaluate cost function
    J = cofi_cost_func_v(X_r, W_r, b_r, Y_r, R_r, 0)
    print(f"Cost: {J:0.2f}")

    # Evaluate cost function with regularization
    J = cofi_cost_func_v(X_r, W_r, b_r, Y_r, R_r, 1.5)
    print(f"Cost (with regularization): {J:0.2f}")
    movieList, movieList_df = load_Movie_List_pd()

    my_ratings = np.zeros(num_movies)  # Initialize my ratings

    for row in res:
        my_ratings[row[0]] = row[1]

    # Check the file small_movie_list.csv for id of each movie in our dataset
    # For example, Toy Story 3 (2010) has ID 2700, so to rate it "5", you can set
    my_ratings[2700] = 5

    # Or suppose you did not enjoy Persuasion (2007), you can set
    my_ratings[2609] = 2

    # We have selected a few movies we liked / did not like and the ratings we
    # gave are as follows:
    # my_ratings[929] = 5   # Lord of the Rings: The Return of the King, The
    # my_ratings[246] = 5   # Shrek (2001)
    # my_ratings[2716] = 3   # Inception
    # my_ratings[1150] = 5   # Incredibles, The (2004)
    # my_ratings[382] = 2   # Amelie (Fabuleux destin d'Amélie Poulain, Le)
    # Harry Potter and the Sorcerer's Stone (a.k.a. Harry Potter and the Philosopher's Stone) (2001)
    # my_ratings[366] = 5
    # my_ratings[622] = 5   # Harry Potter and the Chamber of Secrets (2002)
    # my_ratings[988] = 3   # Eternal Sunshine of the Spotless Mind (2004)
    # my_ratings[2925] = 1   # Louis Theroux: Law & Disorder (2008)
    # my_ratings[2937] = 1   # Nothing to Declare (Rien à déclarer)
    # Pirates of the Caribbean: The Curse of the Black Pearl (2003)
    # my_ratings[793] = 5
    my_rated = [i for i in range(len(my_ratings)) if my_ratings[i] > 0]

    print('\nNew user ratings:\n')
    for i in range(len(my_ratings)):
        if my_ratings[i] > 0:
            print(f'Rated {my_ratings[i]} for  {movieList_df.loc[i,"title"]}')
    # Reload ratings
    Y, R = load_ratings_small()

    # Add new user ratings to Y
    Y = np.c_[my_ratings, Y]

    # Add new user indicator matrix to R
    R = np.c_[(my_ratings != 0).astype(int), R]

    # Normalize the Dataset
    Ynorm, Ymean = normalizeRatings(Y, R)
    #  Useful Values
    num_movies, num_users = Y.shape
    num_features = 100

    # Set Initial Parameters (W, X), use tf.Variable to track these variables
    tf.random.set_seed(1234)  # for consistent results
    W = tf.Variable(tf.random.normal(
        (num_users,  num_features), dtype=tf.float64),  name='W')
    X = tf.Variable(tf.random.normal(
        (num_movies, num_features), dtype=tf.float64),  name='X')
    b = tf.Variable(tf.random.normal(
        (1,          num_users),   dtype=tf.float64),  name='b')

    # Instantiate an optimizer.
    optimizer = keras.optimizers.Adam(learning_rate=1e-1)
    iterations = 200
    lambda_ = 1
    for iter in range(iterations):
        # Use TensorFlow’s GradientTape
        # to record the operations used to compute the cost
        with tf.GradientTape() as tape:

            # Compute the cost (forward pass included in cost)
            cost_value = cofi_cost_func_v(X, W, b, Ynorm, R, lambda_)

        # Use the gradient tape to automatically retrieve
        # the gradients of the trainable variables with respect to the loss
        grads = tape.gradient(cost_value, [X, W, b])

        # Run one step of gradient descent by updating
        # the value of the variables to minimize the loss.
        optimizer.apply_gradients(zip(grads, [X, W, b]))

        # Log periodically.
        if iter % 20 == 0:
            print(f"Training loss at iteration {iter}: {cost_value:0.1f}")
    # Make a prediction using trained weights and biases
    p = np.matmul(X.numpy(), np.transpose(W.numpy())) + b.numpy()

    # restore the mean
    pm = p + Ymean

    my_predictions = pm[:, 0]
    movies_to_send = []

    # sort predictions
    ix = tf.argsort(my_predictions, direction='DESCENDING')

    for i in range(50):
        j = ix[i]
        if j not in my_rated:
            movies_to_send.append(movieList[j])
            print(movieList[j])

    return movies_to_send


if __name__ == "__main__":
    app.run(debug=False, port=8000)
