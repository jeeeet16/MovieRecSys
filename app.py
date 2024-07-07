import pickle
import pandas as pd
import streamlit as st

st.title("Movie Recommendation System")

# The code for backend
movies_dict = pickle.load(open("movie_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)

def generate_google_search_link(movie_title):
    base_url = "https://www.google.com/search?q="
    query = movie_title.replace(" ", "+") 
    search_link = base_url + query
    return search_link

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies_with_links = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        search_link = generate_google_search_link(movie_title)
        recommended_movies_with_links.append((movie_title, search_link))

    return recommended_movies_with_links

similarity = pickle.load(open("similarity.pkl", "rb"))

# The code for frontend
selected_movie = st.selectbox(
    "Enter a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("Recommended Movies:")
    for title, link in recommendations:
        st.markdown(f"- [{title}]({link})")
