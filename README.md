# 🍿 PopcornPicks - Movie Recommendation Engine

> Your personalized movie discovery platform powered by AI. Find your next favorite film in seconds!

[![Live Site](https://img.shields.io/badge/🌐_Live-popcornpicks--frontend--154l.onrender.com-blue?style=for-the-badge)](https://popcornpicks-frontend-154l.onrender.com)
[![Backend API](https://img.shields.io/badge/API-popcornpicks_backend--pa5m-green?style=for-the-badge)](https://popcornpicks-backend-pa5m.onrender.com)
[![API Docs](https://img.shields.io/badge/Swagger-Docs-orange?style=for-the-badge)](https://popcornpicks-backend-pa5m.onrender.com/docs)

---

## 📋 Table of Contents

- [🎯 Overview](#overview)
- [✨ Features](#features)
- [🏗️ Architecture](#architecture)
- [🛠️ Tech Stack](#tech-stack)
- [📁 Project Structure](#project-structure)
- [🚀 Quick Start](#quick-start)
- [🔧 Local Development](#local-development)
- [📘 API Documentation](#api-documentation)
- [👤 Authentication](#authentication)
- [💾 Database](#database)
- [🌐 Deployment](#deployment)
- [📱 Screenshots & Features](#screenshots--features)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

---

## 🎯 Overview

**PopcornPicks** is a comprehensive, production-ready movie recommendation platform built across three phases:

- **Phase 1**: Basic multi-page Streamlit app with content-based recommendations
- **Phase 2**: User authentication, persistent storage, watchlists, ratings, and notes
- **Phase 3**: Scalable FastAPI backend with intelligent recommendations

The system analyzes movies by **genre, cast, crew, and community ratings** to suggest films you'll love.

### Live Demo
- **Frontend**: [https://popcornpicks-frontend-154l.onrender.com](https://popcornpicks-frontend-154l.onrender.com)
- **Backend API**: [https://popcornpicks-backend-pa5m.onrender.com](https://popcornpicks-backend-pa5m.onrender.com)
- **Swagger Docs**: [https://popcornpicks-backend-pa5m.onrender.com/docs](https://popcornpicks-backend-pa5m.onrender.com/docs)

---

## ✨ Features

### 🏠 Home - Find Your Next Movie
- **Smart Search**: Find movies and get instant recommendations
- **Genre Filtering**: Narrow down results by movie genre
- **Dynamic Recommendations**: Shows why each movie is recommended (shared cast/crew/genre)
- **Live Trailers**: Watch trailers directly in the app
- **Movie Details**: Full overview, ratings, runtime, tagline

### 🔥 Trending - Fresh Picks Weekly
- **Real-time Trending**: Updated daily from TMDB
- **Top 10 Movies**: This week's most popular films
- **Quick Save**: Add trending movies to your watchlist

### ❤️ Watchlist - Your Personal Collection
- **Persistent Storage**: Remember all your saved movies
- **User Ratings**: Rate movies on a 1-10 scale
- **Custom Notes**: Add personal notes to track thoughts
- **Quick Management**: Remove or update anytime
- **Per-User**: Each user has their own private watchlist

### 👤 User Profiles
- **Secure Authentication**: Login with username/password
- **Search History**: Tracks your movie searches
- **Per-User Data**: Isolated watchlists, ratings, and notes
- **Session Persistence**: Stay logged in across sessions

### 📊 Backend Intelligence
- **Content-Based Filtering**: Analyzes movie metadata
- **Similarity Scoring**: Uses cosine similarity on embeddings
- **Fast API**: Sub-second response times
- **RESTful Design**: Easy integration and scaling

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│               Frontend (Streamlit)                       │
│   https://popcornpicks-frontend-154l.onrender.com      │
├────────────────────────────────────────────────────────┤
│  Pages:                                                 │
│  • 🏠 Home      → Search & Recommendations              │
│  • 🔥 Trending  → Popular Movies                        │
│  • ❤️ Watchlist → Saved Movies with Notes & Ratings   │
│  • 👤 Auth      → Login/Logout                          │
└──────────────────────┬──────────────────────────────────┘
                       │ REST API
                       ▼
┌─────────────────────────────────────────────────────────┐
│            Backend (FastAPI)                            │
│   https://popcornpicks-backend-pa5m.onrender.com       │
├────────────────────────────────────────────────────────┤
│  Endpoints:                                             │
│  • POST /recommend    → Get similar movies              │
│  • GET  /search       → Find movies by query            │
│  • GET  /genres       → Available genres                │
│  • GET  /movies       → All movies list                 │
│  • GET  /health       → API status                      │
│  • Swagger /docs      → Interactive API explorer        │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   ┌─────────┐  ┌──────────┐  ┌──────────────┐
   │ Models  │  │ Database │  │ TMDB Proxy   │
   │ (pickle)│  │ (SQLite) │  │ (Cloudflare) │
   └─────────┘  └──────────┘  └──────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
- **Streamlit** `>=1.32.0` - Interactive web UI framework
- **Python 3.11+** - Core language
- **Requests** - HTTP client for API calls
- **streamlit-authenticator 0.4.2** - User authentication

### Backend
- **FastAPI** `>=0.110.0` - Modern async web framework
- **Uvicorn** `>=0.29.0` - ASGI server
- **sentence-transformers** `>=2.7.0` - NLP embeddings
- **PyTorch** `>=2.2.0` - Deep learning framework
- **Pydantic** `>=2.0.0` - Data validation
- **scikit-learn** `>=1.4.0` - ML algorithms

### Database & Auth
- **SQLAlchemy** `>=2.0.0` - ORM for database operations
- **SQLite** - Local development database (PostgreSQL for production)
- **bcrypt** `>=4.0.0` - Secure password hashing
- **PyYAML** - Configuration management

### Data Processing
- **Pandas** `>=2.1.0` - Data manipulation
- **NumPy** - Numerical computing
- **NLTK** `>=3.8.1` - NLP toolkit
- **pickle** - Model serialization

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **python-dotenv** - Environment management
- **Render** - Deployment platform

---

## 📁 Project Structure

```
PopcornPicks/
├── app.py                          # Main Streamlit router
├── pages/
│   ├── 1_🏠_Home.py               # Movie search & recommendations
│   ├── 2_🔥_Trending.py           # Trending movies
│   └── 3_❤️_Watchlist.py          # User watchlist management
├── backend/
│   ├── main.py                    # FastAPI application
│   ├── recommender.py             # Recommendation logic
│   └── schemas.py                 # Pydantic data models
├── utils/
│   ├── api.py                     # API client functions
│   ├── auth.py                    # Authentication helpers
│   ├── database.py                # SQLAlchemy models & CRUD
│   └── state.py                   # Streamlit session state
├── modelmaking.ipynb              # ML model training notebook
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
├── .env.example                   # Template for .env
├── docker-compose.yml             # Docker Compose config
├── Dockerfile.frontend            # Frontend container
├── Dockerfile.backend             # Backend container
├── popcornpicks.db               # SQLite database
├── movie_list.pkl                # Pre-computed movie data
├── similarity.pkl                # Pre-computed similarity matrix
├── auth_config.yaml              # Authentication config
└── README.md                      # This file
```

---

## 🚀 Quick Start

### Option 1: Live Demo (No Setup Required!)
Simply visit: **[https://popcornpicks-frontend-154l.onrender.com](https://popcornpicks-frontend-154l.onrender.com)**

**Demo Credentials:**
- Username: `priyanshu`
- Password: `admin123`

### Option 2: Local Development

#### Prerequisites
- Python 3.11+
- pip or conda
- Git

#### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/PopcornPicks.git
cd PopcornPicks
```

#### Step 2: Create & Activate Environment
```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Using conda
conda create -n popcorn python=3.11
conda activate popcorn
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Setup Environment Variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

#### Step 5: Start the Backend
```bash
# Terminal 1
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

#### Step 6: Start the Frontend
```bash
# Terminal 2
streamlit run app.py
```

The app will open at: **http://localhost:8501**

---

## 🔧 Local Development

### Backend Development

#### Check Backend Health
```bash
curl http://localhost:8000/health
```

#### View API Documentation
Open **http://localhost:8000/docs** (Swagger UI)
or **http://localhost:8000/redoc** (ReDoc)

#### Test Recommendations Endpoint
```bash
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"movie": "The Dark Knight", "genre_filter": "All", "top_n": 5}'
```

### Frontend Development

#### Hot Reload
Streamlit automatically reloads when you save files.

#### Debug Mode
Edit `.streamlit/config.toml` (create if needed):
```toml
[logger]
level = "debug"

[client]
showErrorDetails = true
```

#### Clear Cache
```bash
streamlit cache clear
```

---

## 📘 API Documentation

### Base URL
- **Local**: `http://localhost:8000`
- **Production**: `https://popcornpicks-backend-pa5m.onrender.com`

### Endpoints

#### 1. Get Recommendations
**POST** `/recommend`

Request:
```json
{
  "movie": "The Dark Knight",
  "genre_filter": "All",
  "top_n": 5
}
```

Response:
```json
{
  "query": "The Dark Knight",
  "results": [
    {
      "title": "The Dark Knight Rises",
      "movie_id": 49026,
      "year": "2012",
      "rating": 8.5,
      "why": ["🎭 Action", "🎬 Christian Bale", "🎥 Christopher Nolan"]
    }
  ]
}
```

#### 2. Search Movies
**GET** `/search?q=avatar&limit=10`

Response:
```json
{
  "results": [
    {
      "title": "Avatar",
      "movie_id": 19995,
      "year": "2009"
    }
  ]
}
```

#### 3. Get Genres
**GET** `/genres`

Response:
```json
{
  "genres": ["Action", "Adventure", "Animation", "Comedy", ...]
}
```

#### 4. Get All Movies
**GET** `/movies`

Response:
```json
{
  "movies": ["The Shawshank Redemption", "The Godfather", ...],
  "count": 4809
}
```

#### 5. Health Check
**GET** `/health`

Response:
```json
{
  "status": "healthy",
  "movies_loaded": 4809
}
```

### Interactive API Explorer
Visit Swagger UI: **[https://popcornpicks-backend-pa5m.onrender.com/docs](https://popcornpicks-backend-pa5m.onrender.com/docs)**

---

## 👤 Authentication

### Database Models

#### Users (via `streamlit-authenticator`)
- Credentials stored in `auth_config.yaml`
- Passwords hashed with bcrypt
- Session management via cookies

#### Database Tables

**Watchlist**
- Stores user-saved movies
- Per-user isolation
- Includes poster URL, ratings, notes

**SearchHistory**
- Tracks movie searches
- Timestamped entries
- Used for recent searches display

**MovieRating**
- User-provided ratings (1-10)
- Per-user per-movie
- Separate from TMDB ratings

### Demo Account
```
Username: priyanshu
Password: admin123
```

To add new users, edit `auth_config.yaml`:
```yaml
credentials:
  usernames:
    newuser:
      email: user@example.com
      first_name: First
      last_name: Last
      password: <bcrypt_hash>
      roles: [user]
```

---

## 💾 Database

### Local Development
**SQLite**: `popcornpicks.db`

### Production
**PostgreSQL**: Set `DATABASE_URL` environment variable

### Schema

```sql
-- Watchlist
CREATE TABLE watchlist (
  id INTEGER PRIMARY KEY,
  username TEXT,
  movie_id INTEGER,
  title TEXT,
  poster_url TEXT,
  rating FLOAT,
  note TEXT,
  added_at DATETIME
);

-- Search History
CREATE TABLE search_history (
  id INTEGER PRIMARY KEY,
  username TEXT,
  movie TEXT,
  searched_at DATETIME
);

-- Movie Ratings
CREATE TABLE movie_ratings (
  id INTEGER PRIMARY KEY,
  username TEXT,
  movie_id INTEGER,
  title TEXT,
  rating FLOAT,
  rated_at DATETIME
);
```

### Database Operations

#### Generate SQLite Database
```bash
python -c "from utils.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

#### View SQLite Data
```bash
sqlite3 popcornpicks.db
sqlite> SELECT COUNT(*) FROM watchlist;
```

---

## 🌐 Deployment

### Render Deployment

#### Frontend (Streamlit)
1. Push code to GitHub
2. Create new Render app: `streamlit run app.py`
3. Set environment variables in Render dashboard
4. Connect to GitHub repository

**Render Settings:**
```
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.port 10000
Environment:
  BACKEND_URL=https://popcornpicks-backend-pa5m.onrender.com
  DATABASE_URL=postgresql://...
```

#### Backend (FastAPI)
1. Create new Render Service
2. Set start command: `uvicorn backend.main:app --host 0.0.0.0 --port 10000`

**Render Settings:**
```
Build Command: pip install -r requirements.txt
Start Command: uvicorn backend.main:app --host 0.0.0.0 --port 10000
Environment:
  POSTGRES_URL=postgresql://...
```

### Docker Deployment

#### Build & Run Locally
```bash
# Build images
docker-compose build

# Run containers
docker-compose up

# Access:
# Frontend: http://localhost:8501
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

#### Deploy to Docker Hub/Registry
```bash
docker build -f Dockerfile.backend -t popcornpicks-backend:latest .
docker build -f Dockerfile.frontend -t popcornpicks-frontend:latest .
docker push <registry>/popcornpicks-backend:latest
docker push <registry>/popcornpicks-frontend:latest
```

### Environment Variables

**Frontend (.env)**
```
PROXY_BASE_URL=https://tmdb-proxy.priyanshukv06.workers.dev
BACKEND_URL=https://popcornpicks-backend.onrender.com
DATABASE_URL=sqlite:///popcornpicks.db
```

**Backend (.env)**
```
DATABASE_URL=postgresql://user:pass@host:5432/dbname
TMDB_API_KEY=your_tmdb_key (optional, via proxy)
```

---

## 📱 Screenshots & Features

### Home Page - Find Movies
- Interactive movie selector with autocomplete
- Genre-based filtering
- Real-time recommendations with explanation
- Quick save to watchlist
- Share why the movie was recommended

### Trending Page
- Updated daily from TMDB
- Top 10 movies this week
- Quick access to watchlist

### Watchlist Page
- All saved movies in one place
- Rate movies (1-10 scale)
- Add personal notes
- Track when added
- Easy removal

### User Sidebar
- Welcome message with user name
- Recent search history (from database)
- Quick logout
- Persistent across all pages

---

## 🤝 Contributing

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Code Standards
- Follow PEP 8 for Python code
- Add docstrings to functions
- Keep components modular
- Add type hints where possible
- Test before submitting PR

### Development Workflow
```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes and test locally
# (both frontend and backend)

# Run linting (optional)
# pip install black flake8
# black .
# flake8 .

# Commit and push
git add .
git commit -m "Add your feature"
git push origin feature/your-feature

# Create Pull Request on GitHub
```

### Areas for Contribution
- [ ] Collaborative filtering recommendations
- [ ] User preference learning
- [ ] Export watchlist as JSON/CSV
- [ ] Social sharing features
- [ ] Mobile-optimized UI
- [ ] Additional languages
- [ ] Advanced analytics dashboard
- [ ] Machine learning model improvements

---

## 📚 Model Training

The recommendation model is trained in **`modelmaking.ipynb`** using:

1. **Data**: TMDB dataset (4,809 movies)
2. **Features**: Genres, cast, crew, keywords
3. **Similarity**: Cosine similarity on TF-IDF vectors
4. **Output**: `similarity.pkl` and `movie_list.pkl`

To retrain:
```bash
jupyter notebook modelmaking.ipynb
# Run all cells to regenerate pickle files
```

---

## 🐛 Troubleshooting

### Frontend won't connect to backend
- Check `BACKEND_URL` in `.env`
- Verify backend is running: `curl http://localhost:8000/health`
- Check CORS settings in `backend/main.py`

### Movies not loading
- Ensure `movie_list.pkl` and `similarity.pkl` exist
- Regenerate with `modelmaking.ipynb`
- Check file permissions

### Database errors
- Delete `popcornpicks.db` to reset (development only)
- For PostgreSQL production, check connection string
- Run migrations if schema changes

### Authentication issues
- Clear browser cookies
- Check `auth_config.yaml` exists and is valid YAML
- Verify bcrypt password hashes are correct

### Slow recommendations
- First request caches data (normal)
- Check backend CPU usage
- Verify network latency to backend
- Consider upgrading Render dyno plan

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Priyanshu Verma**
- GitHub: [@priyanshukv06](https://github.com/priyanshukv06)
- Email: priyanshukv06@gmail.com

---

## 🙏 Acknowledgments

- **TMDB** for movie data and API
- **Streamlit** for the amazing web framework
- **FastAPI** for the modern backend framework
- **Sentence Transformers** for NLP capabilities
- **Render** for easy deployment

---

## 🚀 Roadmap

### Phase 4 (Planned)
- [ ] Collaborative filtering integration
- [ ] User-based recommendations
- [ ] Movie ratings aggregation
- [ ] Advanced filtering options
- [ ] Social features (sharing, reviews)

### Phase 5 (Planned)
- [ ] Mobile app (React Native)
- [ ] Series recommendations
- [ ] Mood-based recommendations
- [ ] Watch party features
- [ ] Analytics dashboard

---

## 📞 Support

- **Report Issues**: [GitHub Issues](https://github.com/yourusername/PopcornPicks/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/PopcornPicks/discussions)
- **Email**: priyanshukv06@gmail.com

---

<div align="center">

### 🎬 Happy Movie Watching! 🍿

**[Visit PopcornPicks](https://popcornpicks-frontend.onrender.com)** • **[API Docs](https://popcornpicks-backend.onrender.com/docs)** • **[GitHub](https://github.com/yourusername/PopcornPicks)**

⭐ If you found this helpful, please star the repository!

</div>

