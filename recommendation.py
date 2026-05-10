import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    'title': [
        'Inception',
        'Interstellar',
        'Titanic',
        'The Dark Knight',
        'Avengers'
    ],

    'genre': [
        'Sci-Fi Action',
        'Sci-Fi Drama',
        'Romance Drama',
        'Action Crime',
        'Action Superhero'
    ]
}


df = pd.DataFrame(movies)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])

similarity = cosine_similarity(count_matrix)


def recommend(movie_name):
    movie_index = df[df['title'] == movie_name].index[0]

    scores = list(enumerate(similarity[movie_index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("Recommended Movies:\n")

    for movie in sorted_scores[1:]:
        print(df.iloc[movie[0]]['title'])


movie = input("Enter movie name: ")
recommend(movie)