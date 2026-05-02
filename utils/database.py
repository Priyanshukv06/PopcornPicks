from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///popcornpicks.db")

# SQLite needs this fix for Streamlit's threading
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# ── Models ────────────────────────────────────────────────────────────────────
class Watchlist(Base):
    __tablename__ = "watchlist"
    id         = Column(Integer, primary_key=True, index=True)
    username   = Column(String, index=True)
    movie_id   = Column(Integer)
    title      = Column(String)
    poster_url = Column(String)
    rating     = Column(Float)
    note       = Column(Text, default="")
    added_at   = Column(DateTime, default=datetime.utcnow)

class SearchHistory(Base):
    __tablename__ = "search_history"
    id         = Column(Integer, primary_key=True, index=True)
    username   = Column(String, index=True)
    movie      = Column(String)
    searched_at = Column(DateTime, default=datetime.utcnow)

class MovieRating(Base):
    __tablename__ = "movie_ratings"
    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    movie_id = Column(Integer)
    title    = Column(String)
    rating   = Column(Float)
    rated_at = Column(DateTime, default=datetime.utcnow)


# ── Create all tables ─────────────────────────────────────────────────────────
Base.metadata.create_all(bind=engine)


# ── CRUD Helpers ──────────────────────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_to_watchlist(username, movie_id, title, poster_url, rating):
    db = SessionLocal()
    exists = db.query(Watchlist).filter_by(username=username, movie_id=movie_id).first()
    if not exists:
        db.add(Watchlist(username=username, movie_id=movie_id,
                         title=title, poster_url=poster_url, rating=rating))
        db.commit()
        db.close()
        return True
    db.close()
    return False  # already exists

def remove_from_watchlist(username, movie_id):
    db = SessionLocal()
    db.query(Watchlist).filter_by(username=username, movie_id=movie_id).delete()
    db.commit()
    db.close()

def get_watchlist(username):
    db = SessionLocal()
    items = db.query(Watchlist).filter_by(username=username)\
               .order_by(Watchlist.added_at.desc()).all()
    db.close()
    return items

def update_note(username, movie_id, note):
    db = SessionLocal()
    item = db.query(Watchlist).filter_by(username=username, movie_id=movie_id).first()
    if item:
        item.note = note
        db.commit()
    db.close()

def add_search_history(username, movie):
    db = SessionLocal()
    db.add(SearchHistory(username=username, movie=movie))
    db.commit()
    db.close()

def get_search_history(username, limit=10):
    db = SessionLocal()
    items = db.query(SearchHistory).filter_by(username=username)\
               .order_by(SearchHistory.searched_at.desc()).limit(limit).all()
    db.close()
    return items

def save_rating(username, movie_id, title, rating):
    db = SessionLocal()
    existing = db.query(MovieRating).filter_by(username=username, movie_id=movie_id).first()
    if existing:
        existing.rating = rating
        existing.rated_at = datetime.utcnow()
    else:
        db.add(MovieRating(username=username, movie_id=movie_id,
                           title=title, rating=rating))
    db.commit()
    db.close()

def get_ratings(username):
    db = SessionLocal()
    items = db.query(MovieRating).filter_by(username=username).all()
    db.close()
    return items
