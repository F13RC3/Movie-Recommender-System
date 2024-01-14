import streamlit as st
import pickle
import requests
import pandas as pd


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYWE2MzAwMzRiODI1NzU4NmZhYWRkM2YzMTk1MzMzNSIsInN1YiI6IjY1NmYxMjM0NTY4NDYzMDEwZjg0OGFjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TqkfknyqGDXVLzyIPcHYyyOrkmz3Fvm1ag38DcRQA-k"
    }
    data = requests.get(url, headers=headers)
    data = data.json()
    poster_path = data['poster_path']
    # print('poster path json : ', poster_path)
    
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie, new_df, similarity):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommended_movie=[]
    recommended_movie_posters=[]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        try:
            movie_id = new_df.iloc[i[0]].movie_id
            recommended_movie.append(new_df.iloc[i[0]].title)
            # print(new_df.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))
        except:
            continue
    return recommended_movie, recommended_movie_posters

movies_dict = pickle.load(open('movie.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select the Movie',movies['title'].values)

if st.button('Recommend'):
    recommended_movie, recommended_movie_posters = recommend(selected_movie_name, movies, similarity)
    col= st.columns(5)
    for name, poster, c in zip(recommended_movie,recommended_movie_posters, col):
        with c:
            st.text(name)
            st.image(poster)
        