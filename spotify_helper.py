from config import sp

# Song image from Spotify
def get_song_image_url(song_name):
    search_query = f"track:{song_name}"
    try:
        results = sp.search(q=search_query, type="track")
        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            image_url = track["album"]["images"][0]["url"]
            return image_url
        else:
            return "https://www.figma.com/community/resource/0c2e9ce7-9ccc-4a64-bc58-591beae094f6/thumbnail"
    except Exception:
        return "https://www.figma.com/community/resource/0c2e9ce7-9ccc-4a64-bc58-591beae094f6/thumbnail"
