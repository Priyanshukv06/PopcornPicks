# Movie Recommender System

## Overview
The **Movie Recommender System** is a content-based recommendation system that suggests movies based on user selection. It utilizes a similarity matrix to find and display the top 5 most similar movies, along with their posters.

## Features
- Movie recommendations based on content similarity.
- Fetches movie posters using **TMDB API**.
- Interactive user interface using **Streamlit**.
- Fast and lightweight recommendation system.
- Model trained using a Jupyter Notebook file (**modelmaking.ipynb**).

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd movie-recommender-system
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Jupyter Notebook to generate the required pickle files:
   ```bash
   jupyter notebook modelmaking.ipynb
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Select a movie from the dropdown.
4. Click on "Show Recommendation" to see the top 5 recommended movies and their posters.

## Model Training
- The recommendation model is built and preprocessed in **modelmaking.ipynb**.
- Running this notebook will generate the required **pickle files** locally.
- The local dataset file has been removed due to size constraints.

## Deployment
- The application will be hosted on **Streamlit** for easy access.

## Dependencies
- Python 3.x
- Streamlit
- Requests
- Pandas
- Pickle
- Jupyter Notebook

## Project Structure
```
📂 movie-recommender-system
├── app.py                # Main Streamlit app
├── modelmaking.ipynb     # Jupyter notebook for model training
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Future Enhancements
- Improve recommendation accuracy using collaborative filtering.
- Add genre-based filtering.
- Enhance UI with better visuals.
- Optimize API calls to reduce response time.

## License
This project is open-source and available for use under the **MIT License**.

## Author
Developed by **Priyanshu Verma** 🚀

