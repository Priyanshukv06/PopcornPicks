import streamlit as st
from utils.api import fetch_trending, fetch_movie_details
from utils.state import init_state, add_favorite

init_state()

st.title("🔥 Trending This Week")
st.markdown("*Updated every 24 hours from TMDB*")

with st.spinner("Loading trending movies..."):
    trending = fetch_trending()

if not trending:
    st.error("Could not load trending movies. Check your proxy.")
    st.stop()

cols = st.columns(5)
for i, movie in enumerate(trending):
    with cols[i % 5]:
        poster = ("https://image.tmdb.org/t/p/w500" + movie['poster_path']
                 if movie.get('poster_path') else
                 "https://via.placeholder.com/500x750?text=No+Poster")
        st.image(poster, width='stretch')
        st.caption(f"**{movie['title']}**")
        st.caption(f"⭐ {round(movie.get('vote_average', 0), 1)}/10")
        st.button("❤️ Save", key=f"trend_fav_{movie['id']}",
                  on_click=add_favorite, args=(movie['title'],))
