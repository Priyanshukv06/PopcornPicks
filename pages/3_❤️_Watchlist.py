import streamlit as st
from utils.state import init_state
from utils.database import get_watchlist, remove_from_watchlist, update_note, save_rating

init_state()

if 'username' not in st.session_state:
    st.warning("Please log in first.")
    st.stop()

username = st.session_state.username

st.title("❤️ My Watchlist")
st.markdown("*Your saved movies — add notes and ratings*")

watchlist = get_watchlist(username)

if not watchlist:
    st.info("Your watchlist is empty! Go to 🏠 Home to save movies.")
    st.stop()

st.markdown(f"**{len(watchlist)} movies saved**")
st.markdown("---")

cols = st.columns(4)
for i, item in enumerate(watchlist):
    with cols[i % 4]:
        st.image(item.poster_url, width='stretch')
        st.caption(f"**{item.title}**")
        st.caption(f"⭐ TMDB: {item.rating}/10")

        # User rating
        user_rating = st.slider(
            "Your rating", 1.0, 10.0, 5.0,
            step=0.5, key=f"rate_{item.movie_id}"
        )
        if st.button("💾 Save Rating", key=f"saverate_{item.movie_id}"):
            save_rating(username, item.movie_id, item.title, user_rating)
            st.toast(f"Rating saved for {item.title}!")

        # Notes
        note = st.text_area(
            "📝 Notes", value=item.note or "",
            key=f"note_{item.movie_id}", height=80
        )
        if st.button("💾 Save Note", key=f"savenote_{item.movie_id}"):
            update_note(username, item.movie_id, note)
            st.toast("Note saved!")

        # Remove
        if st.button("🗑️ Remove", key=f"rm_{item.movie_id}"):
            remove_from_watchlist(username, item.movie_id)
            st.rerun()
