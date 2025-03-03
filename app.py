import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from flask import Flask, request, jsonify

# Loading the Spotify dataset
df = pd.read_csv("tracks.csv")

# Selecting music features for recommendations
features = ['danceability', 'energy', 'tempo']
df[features] = df[features].fillna(df[features].mean())

# Normalize the features
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Fit Nearest Neighbors model
knn = NearestNeighbors(n_neighbors=6, metric='cosine', algorithm='brute')
knn.fit(df[features])

def recommend_songs(song_name, top_n=5):
    """Recommend similar songs using Nearest Neighbors."""
    idx = df[df['name'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        return []
    
    idx = idx[0]
    distances, indices = knn.kneighbors([df.iloc[idx][features]], n_neighbors=top_n+1)
    
    return [df.iloc[i]['name'] for i in indices[0][1:]]

# Flask App
app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    song_name = request.args.get('song')
    if not song_name:
        return jsonify({"error": "Please provide a song name."}), 400
    
    recommendations = recommend_songs(song_name)
    if not recommendations:
        return jsonify({"error": "Song not found in the dataset."}), 404
    
    return jsonify({"recommended_songs": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
