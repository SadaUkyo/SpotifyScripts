import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'http://localhost:8888/callback'  # Must be registered in your Spotify Developer Dashboard

# Set up Spotipy client
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-private,user-library-read'))
    # Get authorization URL
    auth_url = sp.auth_manager.get_authorize_url()
    print("Please visit the following URL to authorize the application:")
    print(auth_url)
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
        print(offset)
        offset += limit

    print(f"Total liked songs fetched: {len(all_liked_songs)}")
    return all_liked_songs

# Get all liked songs
liked_songs = get_all_liked_songs()

# Extract track URIs from the liked songs
track_uris = [track['track']['uri'] for track in liked_songs]

# Replace the playlist ID below with your actual playlist ID
playlist_id = 'your_playlist_id'

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
# Add the liked songs to the specified playlist in chunks
try:
    # Define a function to split the list into smaller chunks
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    # Split the list of track URIs into smaller chunks
    chunk_size = 100  # Adjust the chunk size as needed
    track_uri_chunks = list(chunks(track_uris, chunk_size))

    # Add tracks to the playlist in chunks
    for chunk in track_uri_chunks:
        sp.playlist_add_items(playlist_id, chunk)
    
    print("Liked songs added to the playlist successfully.")
except spotipy.exceptions.SpotifyException as e:
    print("Failed to add liked songs to the playlist.")
    print(e)
    exit()
