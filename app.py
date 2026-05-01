import os
import pickle
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
PROXY_BASE_URL = os.getenv("PROXY_BASE_URL", "https://tmdb-proxy.priyanshukv06.workers.dev")

# Page config
st.set_page_config(
    page_title="PopcornPicks 🍿",
    page_icon="🎬",
    layout="wide"
)

@st.cache_data
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

def fetch_poster(movie_id):
    try:
        url = f"{PROXY_BASE_URL}/movie/{movie_id}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    except Exception:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)
    return names, posters

# Load data
try:
    movies, similarity = load_data()
except FileNotFoundError as e:
    st.error(f"❌ Required file not found: {e}. Make sure `movie_list.pkl` and `similarity.pkl` are in the project folder.")
    st.stop()

# UI
st.title("🍿 PopcornPicks")
st.markdown("*Find movies similar to what you love*")

selected_movie = st.selectbox("🎬 Type or select a movie", movies['title'].values)

if st.button("Show Recommendations", type="primary"):
    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie, movies, similarity)

    st.markdown("### You might also like:")
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.caption(f"**{name}**")