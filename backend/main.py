from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import RecommendRequest, RecommendResponse, SearchResponse
from backend import recommender

app = FastAPI(
    title="PopcornPicks API",
    description="Movie recommendation engine powered by Sentence Transformers",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"status": "online", "message": "PopcornPicks API v2.0"}

@app.post("/recommend", response_model=RecommendResponse)
def get_recommendations(req: RecommendRequest):
    results = recommender.recommend(req.movie, req.genre_filter, req.top_n)
    if not results:
        raise HTTPException(status_code=404, detail=f"Movie '{req.movie}' not found")
    return {"query": req.movie, "results": results}

@app.get("/search", response_model=SearchResponse)
def search(q: str, limit: int = 10):
    results = recommender.search_movies(q, limit)
    return {"results": results}

@app.get("/genres")
def get_genres():
    return {"genres": recommender.get_all_genres()}

@app.get("/movies")
def get_all_movies():
    titles = recommender.movies['title'].tolist()
    return {"movies": titles, "count": len(titles)}

@app.get("/health")
def health():
    return {"status": "healthy", "movies_loaded": len(recommender.movies)}