import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load once when backend starts
movies     = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def get_common_tags(idx1: int, idx2: int) -> list:
    def to_set(val):
        return set(str(val).lower().replace(" ", "").split())
    common  = [f"🎭 {g}" for g in to_set(movies.iloc[idx1]['genres']) & to_set(movies.iloc[idx2]['genres'])]
    common += [f"🎬 {c}" for c in to_set(movies.iloc[idx1]['cast'])   & to_set(movies.iloc[idx2]['cast'])]
    common += [f"🎥 {d}" for d in to_set(movies.iloc[idx1]['crew'])   & to_set(movies.iloc[idx2]['crew'])]
    return common[:5]

def recommend(movie: str, genre_filter: str = "All", top_n: int = 5) -> list:
    matches = movies[movies['title'] == movie]
    if matches.empty:
        return []

    index     = matches.index[0]
    distances = sorted(list(enumerate(similarity[index])),
                       reverse=True, key=lambda x: x[1])
    results = []
    for i, score in distances[1:]:
        row = movies.iloc[i]
        if genre_filter and genre_filter != "All":
            if genre_filter.lower() not in str(row['genres']).lower():
                continue
        results.append({
            "title":    row['title'],
            "movie_id": int(row['movie_id']),
            "year":     str(int(row['year'])) if str(row['year']) != 'nan' else 'N/A',
            "rating":   round(float(row['vote_average']), 1),
            "why":      get_common_tags(index, i)
        })
        if len(results) == top_n:
            break
    return results

def search_movies(query: str, limit: int = 10) -> list:
    mask    = movies['title'].str.contains(query, case=False, na=False)
    results = movies[mask][['title', 'movie_id', 'year']].head(limit)
    return [
        {
            "title":    row['title'],
            "movie_id": int(row['movie_id']),
            "year":     str(int(row['year'])) if str(row['year']) != 'nan' else 'N/A'
        }
        for _, row in results.iterrows()
    ]

def get_all_genres() -> list:
    genres = set()
    for g in movies['genres'].dropna():
        genres.update(str(g).split())
    return sorted(genres)