import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "5aabba6e9f6844a2a95bcdd3b8f35d56"
CLIENT_SECRET = "0c4e7238d5ae47a29884863863cef199"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
