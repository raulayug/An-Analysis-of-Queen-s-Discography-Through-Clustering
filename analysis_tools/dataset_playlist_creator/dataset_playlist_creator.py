import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

def create_playlist(sp, user_id, name, description, tracks):
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False, description=description)
    playlist_id = playlist['id']
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tracks)
    return playlist_id

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
    with open('dataset_playlist_creator_input.txt', 'r') as file:
        lines = file.readlines()

    # Parse input text and create playlist
    tracks = []
    for line in lines:
        track_id = line.strip()
        tracks.append(track_id)

    # Create playlist
    playlist_name = 'Queen Dataset'
    playlist_description = "An Analysis Of Queen's Discography Using KMeans, DBScan, And Affinity Propagation Clustering Techniques Based On Full And Reduced Musical Feature Sets - by Earl Edison B. Felizardo & Josemaria Y. Layug III"
    playlist_id = create_playlist(sp, USERNAME, playlist_name, playlist_description, tracks)
    print(f"Playlist '{playlist_name}' created with ID '{playlist_id}'")

if __name__ == "__main__":
    main()
