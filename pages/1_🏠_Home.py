import streamlit as st
from utils.api import get_recommendations, fetch_movie_details, fetch_trailer, get_genres_api
from utils.state import init_state
from utils.database import add_to_watchlist, add_search_history
import requests
import os
from dotenv import load_dotenv

load_dotenv()
init_state()
username = st.session_state.get("username", "guest")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.markdown("""
<style>
.movie-card img { border-radius: 10px; width: 100%; transition: transform 0.2s; }
.movie-card:hover img { transform: scale(1.05); }
.tag-pill {
    display: inline-block; background: #e50914; color: white;
    border-radius: 12px; padding: 2px 10px; margin: 2px; font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏠 Find Your Next Movie")

genres       = get_genres_api()
genre_filter = st.selectbox("🎭 Filter by Genre", genres)

# Load movie list for selectbox
try:
    all_movies = requests.get(f"{BACKEND_URL}/movies", timeout=5).json()['movies']
except Exception:
    all_movies = []

selected_movie = st.selectbox("🎬 Type or select a movie", all_movies)

if st.button("Show Recommendations", type="primary"):
    add_search_history(username, selected_movie)
    with st.spinner("Finding similar movies..."):
        st.session_state.results    = get_recommendations(selected_movie, genre_filter)
        st.session_state.last_movie = selected_movie

if st.session_state.get('results'):
    st.markdown(f"### Because you liked **{st.session_state.last_movie}**:")
    cols = st.columns(5)
    for col, movie in zip(cols, st.session_state.results):
        details = fetch_movie_details(movie['movie_id'])
        with col:
            st.markdown(
                f'<div class="movie-card"><img src="{details["poster"]}"/></div>',
                unsafe_allow_html=True)
            st.caption(f"**{movie['title']}** ({movie['year']})")
            st.caption(f"⭐ {movie['rating']}/10")

            def save_to_db(mid=movie['movie_id'], t=movie['title'],
                           p=details['poster'], r=movie['rating']):
                added = add_to_watchlist(username, mid, t, p, r)
                st.toast(f"❤️ '{t}' added!" if added else f"Already saved!")

            st.button("❤️ Save", key=f"fav_{movie['movie_id']}", on_click=save_to_db)

            with st.expander("🤔 Why this?"):
                if movie.get('why'):
                    for reason in movie['why']:
                        st.markdown(f'<span class="tag-pill">{reason}</span>',
                                   unsafe_allow_html=True)
                else:
                    st.caption("Similar overall vibe!")

            with st.expander("ℹ️ Details + Trailer"):
                if details['tagline']:
                    st.markdown(f"*{details['tagline']}*")
                st.markdown(f"⭐ {details['rating']}/10 &nbsp;|&nbsp; ⏱️ {details['runtime']} min")
                st.markdown(details['overview'])
                trailer = fetch_trailer(movie['movie_id'])
                if trailer:
                    st.video(trailer)
                else:
                    st.caption("No trailer available.")
