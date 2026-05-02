from pydantic import BaseModel
from typing import List, Optional

class RecommendRequest(BaseModel):
    movie: str
    genre_filter: Optional[str] = "All"
    top_n: Optional[int] = 5

class MovieResult(BaseModel):
    title:    str
    movie_id: int
    year:     str
    rating:   float
    why:      List[str]

class RecommendResponse(BaseModel):
    query:   str
    results: List[MovieResult]

class SearchResult(BaseModel):
    title:    str
    movie_id: int
    year:     str

class SearchResponse(BaseModel):
    results: List[SearchResult]