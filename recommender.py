from models import df, knn, features
from spotify_helper import get_song_album_cover_url

# Recommend songs using Nearest Neighbors
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
