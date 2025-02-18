# Movie Recommender System

## Overview
The **Movie Recommender System** is a content-based recommendation system that suggests movies based on user selection. It utilizes a similarity matrix to find and display the top 5 most similar movies, along with their posters.

## Features
- Movie recommendations based on content similarity.
- Fetches movie posters using **TMDB API**.
- Interactive user interface using **Streamlit**.
- Fast and lightweight recommendation system.
- Model trained using a local dataset and stored in a pickle file.

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
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Select a movie from the dropdown.
3. Click on "Show Recommendation" to see the top 5 recommended movies and their posters.

## Model Training
- The recommendation model is built and preprocessed in **modelmaking.ipynb**.
- The trained model is saved as a pickle file.
- A local dataset has been attached for training purposes.

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
├── movie_list.pkl        # Pickled movie data
├── similarity.pkl        # Pickled similarity matrix
├── dataset/              # Local dataset for training
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

