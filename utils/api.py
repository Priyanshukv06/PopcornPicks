import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
PROXY_BASE_URL = os.getenv("PROXY_BASE_URL", "https://tmdb-proxy.priyanshukv06.workers.dev")
BACKEND_URL    = os.getenv("BACKEND_URL", "http://localhost:8000")

# ── FastAPI calls ─────────────────────────────────────────────────────────────
def get_recommendations(movie: str, genre_filter: str = "All", top_n: int = 5):
    try:
        res = requests.post(f"{BACKEND_URL}/recommend", json={
            "movie": movie,
            "genre_filter": genre_filter,
            "top_n": top_n
        }, timeout=10)
        res.raise_for_status()
        return res.json()['results']
    except Exception as e:
        st.error(f"Backend error: {e}")
        return []

def search_movies_api(query: str):
    try:
        res = requests.get(f"{BACKEND_URL}/search", params={"q": query}, timeout=5)
        return res.json()['results']
    except Exception:
        return []

def get_genres_api():
    try:
        res = requests.get(f"{BACKEND_URL}/genres", timeout=5)
        return ["All"] + res.json()['genres']
    except Exception:
        return ["All"]

# ── TMDB proxy calls (unchanged) ──────────────────────────────────────────────
@st.cache_data(ttl=3600)
def fetch_movie_details(movie_id):
    try:
        data = requests.get(f"{PROXY_BASE_URL}/movie/{movie_id}", timeout=5).json()
        return {
            "poster":   ("https://image.tmdb.org/t/p/w500" + data['poster_path']
                        if data.get('poster_path') else
                        "https://via.placeholder.com/500x750?text=No+Poster"),
            "rating":   data.get('vote_average', 'N/A'),
            "overview": data.get('overview', 'No overview available.'),
            "runtime":  data.get('runtime', 'N/A'),
            "tagline":  data.get('tagline', ''),
            "genres":   [g['name'] for g in data.get('genres', [])]
        }
    except Exception:
        return {"poster": "https://via.placeholder.com/500x750?text=No+Poster",
                "rating": "N/A", "overview": "", "runtime": "N/A",
                "tagline": "", "genres": []}

@st.cache_data(ttl=3600)
def fetch_trailer(movie_id):
    try:
        data = requests.get(f"{PROXY_BASE_URL}/movie/{movie_id}/videos", timeout=5).json()
        for v in data.get('results', []):
            if v['type'] == 'Trailer' and v['site'] == 'YouTube':
                return f"https://www.youtube.com/watch?v={v['key']}"
    except Exception:
        pass
    return None

@st.cache_data(ttl=86400)
def fetch_trending():
    try:
        data = requests.get(f"{PROXY_BASE_URL}/trending/movie/week", timeout=5).json()
        return data.get('results', [])[:10]
    except Exception:
        return []
