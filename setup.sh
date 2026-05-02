#!/bin/bash
echo "🔄 Regenerating similarity matrix..."
python -c "
import pickle, numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open('movie_list.pkl', 'rb'))
model  = SentenceTransformer('all-MiniLM-L6-v2')

print('Encoding...')
embeddings = model.encode(movies['tags'].tolist(), show_progress_bar=True, batch_size=64)

content_sim = cosine_similarity(embeddings)
movies['popularity_score'] = movies['vote_average'] * np.log1p(movies['vote_count'])
movies['popularity_score'] /= movies['popularity_score'].max()
pop_matrix = np.outer(movies['popularity_score'].values, movies['popularity_score'].values)
similarity = 0.85 * content_sim + 0.15 * pop_matrix

pickle.dump(similarity, open('similarity.pkl', 'wb'))
pickle.dump(embeddings, open('embeddings.pkl', 'wb'))
print('Done!')
"
echo "✅ Setup complete"