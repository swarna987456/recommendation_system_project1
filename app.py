import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

st.write('This app uses advanced algorithms and machine learning to analyze movies and recommends new movies that are similar in content and style to the movies you already like')

option = st.selectbox(
    'Select your favourite movie to watch',
    movies['title'])

st.write(f"Hurray!!! {option} :smile: the movie added to your bucket list: ")

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
