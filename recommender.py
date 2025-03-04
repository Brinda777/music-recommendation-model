from models import df, knn, features
from spotify_helper import get_song_image_url

# Recommend songs using Nearest Neighbors
def recommend_songs(song_name, top_n=10):
    idx = df[df['name'].str.lower() == song_name.lower()].index
    if len(idx) == 0:
        return [], []

    idx = idx[0]
    distances, indices = knn.kneighbors([df.iloc[idx][features]], n_neighbors=top_n+1)

    recommendations = []
    seen_songs = set()  
    recommended_names = []

    for i in indices[0][1:]:
        song = df.iloc[i]['name']
        artist = df.iloc[i]['artists'] if 'artists' in df.columns else "Unknown Artist"

        if (song, artist) not in seen_songs:
            seen_songs.add((song, artist))
            image_url = get_song_image_url(song)
            recommendations.append({"song": song, "artist": artist, "image": image_url})
            recommended_names.append(song)

    # Correct Boolean mask using `indices` instead of `distances`
    relevant_songs = df.iloc[indices[0][1:]]['name'].tolist()

    return recommendations, relevant_songs
