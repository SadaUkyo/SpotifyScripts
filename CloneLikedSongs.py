import spotipy
from spotipy.oauth2 import SpotifyOAuth
import configparser

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Set up Spotify API credentials
client_id = config['Spotify']['client_id']
client_secret = config['Spotify']['client_secret']
redirect_uri = 'http://localhost:8888/callback'  # Must be registered in your Spotify Developer Dashboard

# Set up Spotipy client
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-private,user-library-read'))
    user_info = sp.current_user()
    print(f"Successfully connected to Spotify as {user_info['display_name']} ({user_info['id']})")
except spotipy.exceptions.SpotifyException as e:
    print("Failed to connect to Spotify. Please check your credentials and internet connection.")
    print(e)
    exit()

# Function to get all liked songs
def get_all_liked_songs():
    print("Fetching liked songs...")
    offset = 0
    limit = 50
    all_liked_songs = []

    while True:
        liked_songs = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not liked_songs['items']:
            break
        all_liked_songs.extend(liked_songs['items'])
        offset += limit

    print(f"Total liked songs fetched: {len(all_liked_songs)}")
    return all_liked_songs

# Get all liked songs
liked_songs = get_all_liked_songs()

# Extract track URIs from the liked songs
track_uris = [track['track']['uri'] for track in liked_songs]

# Get playlist ID from config
playlist_id = config['CloneLikedSongs']['playlist_id']

print("Clearing existing songs from the playlist...")
# Clear the existing songs from the playlist
try:
    sp.playlist_replace_items(playlist_id, [])
    print("Playlist cleared successfully.")
except spotipy.exceptions.SpotifyException as e:
    print("Failed to clear playlist.")
    print(e)
    exit()

print("Adding liked songs to the playlist...")
# Add the liked songs to the specified playlist
try:
    sp.playlist_add_items(playlist_id, track_uris)
    print("Liked songs added to the playlist successfully.")
except spotipy.exceptions.SpotifyException as e:
    print("Failed to add liked songs to the playlist.")
    print(e)
    exit()
