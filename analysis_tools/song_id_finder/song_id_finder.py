import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

def get_track_id(sp, song_name, album_name):
    # Search for the song with the specified artist and track name
    if album_name != "NOT FOUND":
        # If the album name is not "NOT FOUND", include it in the search
        results = sp.search(q=f'artist:Queen track:{song_name} album:{album_name}', type='track')
    else:
        # If the album name is "NOT FOUND", search only for the track name
        results = sp.search(q=f'artist:Queen track:{song_name}', type='track')

    if results['tracks']['items']:
        # Extract the track ID of the first result
        track_id = results['tracks']['items'][0]['id']
        return track_id
    else:
        return None

def main():
    # Spotify API credentials
    CLIENT_ID = 'CLIENT ID'
    CLIENT_SECRET = 'CLIENT SECRET'
    REDIRECT_URI = 'http://localhost:8888/callback'
    USERNAME = 'USERNAME'
    SCOPE = 'playlist-modify-private'

    # Authenticate and create Spotify API object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE, username=USERNAME))

    # Read input text file
    with open('song_id_finder_input.txt', 'r') as file:
        lines = file.readlines()

    # Print track IDs or "Cannot find song" message
    for i, line in enumerate(lines):
        line = line.strip()
        song_info = line.split('\t')
        if len(song_info) == 2:
            song_name, album_name = song_info
            track_id = get_track_id(sp, song_name, album_name)
            if track_id:
                print(f"{track_id}")
            else:
                print(f"Cannot find song {song_name}")
        else:
            print(f"Invalid input format at line {i+1}")

if __name__ == "__main__":
    main()