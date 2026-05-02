import streamlit as st

def init_state():
    defaults = {
        'favorites': [],
        'history':   [],
        'results':   [],
        'last_movie': None,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def add_favorite(title):
    if title not in st.session_state.favorites:
        st.session_state.favorites.append(title)
        st.toast(f"❤️ Added '{title}' to favorites!")

def add_history(title):
    if title not in st.session_state.history:
        st.session_state.history.append(title)
