import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
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

# Function to get liked songs within the last x days
def get_liked_songs_in_last_x_days(x):
    print(f"Fetching liked songs from the last {x} days...")
    limit = 50
    offset = 0
    all_liked_songs = []

    while True:
        liked_songs = sp.current_user_saved_tracks(limit=limit, offset=offset)
        if not liked_songs['items']:
            break
        
        for track in liked_songs['items']:
            added_at = datetime.strptime(track['added_at'], "%Y-%m-%dT%H:%M:%SZ")
            if datetime.now() - added_at <= timedelta(days=x):
                all_liked_songs.append(track['track'])

        offset += limit

    print(f"Total liked songs from the last {x} days fetched: {len(all_liked_songs)}")
    return all_liked_songs

# Get liked songs from the last x days
x_days = 30  # Change this to the number of days you want
liked_songs_in_last_x_days = get_liked_songs_in_last_x_days(x_days)

# Extract track URIs from the liked songs
track_uris = [track['uri'] for track in liked_songs_in_last_x_days]

# Get playlist ID from config
playlist_id = config['LikedSongsLastXDays']['playlist_id']

print("Clearing existing songs from the playlist...")
# Clear the existing songs from the playlist
try:
    sp.playlist_replace_items(playlist_id, [])
    print("Playlist cleared successfully.")
except spotipy.exceptions.SpotifyException as e:
    print("Failed to clear playlist.")
    print(e)
    exit()

print("Adding liked songs from the last {} days to the playlist...".format(x_days))
# Add the liked songs from the last x days to the specified playlist
try:
    sp.playlist_add_items(playlist_id, track_uris)
    print("Liked songs from the last {} days added to the playlist successfully.".format(x_days))
except spotipy.exceptions.SpotifyException as e:
    print("Failed to add liked songs to the playlist.")
    print(e)
    exit()
