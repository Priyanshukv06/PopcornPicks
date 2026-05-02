import streamlit as st
from utils.state import init_state
from utils.auth import login_page
from utils.database import get_search_history

st.set_page_config(
    page_title="PopcornPicks 🍿",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_state()

authenticator, name, auth_status, username, config, config_path = login_page()

if auth_status is False:
    st.error("❌ Incorrect username or password")
    st.stop()

if auth_status is None:
    st.warning("👆 Please log in to continue")
    st.info("**Demo credentials →** username: `priyanshu` | password: `admin123`")
    st.stop()

# ── Authenticated ─────────────────────────────────────────────────────────────
st.session_state.username = username

with st.sidebar:
    st.title("🍿 PopcornPicks")
    st.markdown(f"👋 Welcome, **{name}**!")
    st.markdown("---")

    # Recent searches from DB
    st.markdown("### 🕐 Recent Searches")
    history = get_search_history(username, limit=5)
    if history:
        for h in history:
            st.caption(f"🔍 {h.movie}")
    else:
        st.caption("No searches yet!")

    st.markdown("---")
    authenticator.logout(location="sidebar")

st.title("🎬 Welcome to PopcornPicks")
st.markdown(f"Hello **{name}**, ready to find your next favourite movie?")
st.markdown("""
| Page | Description |
|---|---|
| 🏠 Home | Search and get recommendations |
| 🔥 Trending | This week's top movies |
| ❤️ Watchlist | Your saved movies with notes |
| 📊 Analytics | Your taste profile |
""")