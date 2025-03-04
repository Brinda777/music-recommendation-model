import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "5aabba6e9f6844a2a95bcdd3b8f35d56"
CLIENT_SECRET = "0c4e7238d5ae47a29884863863cef199"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

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

# verifying spotify song and fetching cover image
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    try:
        results = sp.search(q=search_query, type="track")
        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            album_cover_url = track["album"]["images"][0]["url"]
            return album_cover_url
        else:
            return "https://i.postimg.cc/0QNxYz4V/social.png"
    except Exception as e:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


# Recommend similar songs using Nearest Neighbors.
def recommend_songs(song_name, top_n=5):
    idx = df[df['name'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        return []
    
    idx = idx[0]
    distances, indices = knn.kneighbors([df.iloc[idx][features]], n_neighbors=top_n+1)
    
    recommendations = []
    for i in indices[0][1:]:
        song = df.iloc[i]['name']
        artist = df.iloc[i]['artists'] if 'artists' in df.columns else "Unknown Artist"
        image_url = get_song_album_cover_url(song, artist)
        recommendations.append({"song": song, "artist": artist, "image": image_url})
    
    return recommendations

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
