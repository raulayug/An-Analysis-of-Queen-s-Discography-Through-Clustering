import sys
import spotipy
import spotipy.util
from spotipy.oauth2 import SpotifyOAuth

# Queen song titles and ID Pairs
song_id_list = {
    "Somebody to Love": "4rDbp1vnvEhieiccprPMdI",
    "White Man": "2ekdPqGg9Ta3jDN1I8dm3z",
    "Good Old-Fashioned Lover Boy": "1n7xFAY4xoPeqRvrkzAtsw",
    "A Kind of Magic": "5RYLa5P4qweEAKq5U1gdcK",
    "Friends Will Be Friends": "3EGlnkJGcwz73rT0oE0X1X",
    "One Year of Love": "1SvX2R7kPc0JsGnJaJVzZO",
    "Who Wants to Live Forever": "41kCFJBcaLSt7Ruk5zO3Vr",
    "Princes of the Universe": "0Uy8lcDHiPDicBQ7rnDgcK",
    "39": "65NTcXUtOb27NHKQ4fAcw0",
    "Bohemian Rhapsody": "4u7EnebtmKWzUH433cf5Qv",
    "Love of My Life": "4YJUTdZ0Pgl0ZeNyHYXeLd",
    "You're My Best Friend": "4vhVDkSx9RSb2k6mWFMYNI",
    "Death On Two Legs": "2MvRMWU2ILRcFEU8WWbuP8",
    "Under Pressure": "2fuCquhmrzHpu5xcA1ci9x",
    "All God's People": "6VWhk0VNyGs6o5aTUj4akR",
    "Bijou": "3doVdGo0NrKWDuiAUiWyCY",
    "Don't Try So Hard": "161M6Ul0mY3trIlDxBHyhK",
    "Headlong": "6goUTcMn0V30hWtKFIj6Kh",
    "I Can't Live With You": "4HF7ddEW0eadUpIi3iSqiB",
    "I'm Going Slightly Mad": "1pHVfiNHMMZYquR35fTZdM",
    "Innuendo": "0BzhS74ByIVlyz8BedHaYi",
    "The Show Must Go On": "5n6RDaGFSN88oRWuGtYAIN",
    "These Are the Days of Our Lives": "5js1JJOAkR5KwlifBpvHMN",
    "Bicycle Race": "5CTAcf8aS0a0sIsDwQRF9C",
    "Don't Stop Me Now": "5T8EDUDqKcs6OSOwEsfqG7",
    "Fat Bottomed Girls": "6IAVxNFi1W88UhDeyvOsdo",
    "Fun It": "6jtctBYvybxCAmlg7nT6CS",
    "In Only Seven Days": "06UXtRLTF6kdMSM3uaVCCU",
    "Heaven for Everyone": "3Klfd4rsRO53fYpxmdQmYV",
    "I Was Born to Love You": "7DtdhIJlSSOaAFNk4JdXCb",
    "Made in Heaven": "4NTMIFWtDXnWN4hDSBlKOf",
    "Mother Love": "5ShmaPvHBM0lMG5Tj2VtZF",
    "My Life Has Been Saved": "0W6NenBf8U0HUujewiVQ6y",
    "Too Much Love Will Kill You": "0W1uTK6I97CbjFKAVtRGfK",
    "You Don't Fool Me": "1chxAv59LZcOE5FyrlUze2",
    "My Melancholy Blues": "1WttHhgIl0N0vXZYrOxF0C",
    "Spread Your Wings": "0nUCaKwNqO5whVAhEX1A1R",
    "We Are The Champions": "1lCRw5FEZ1gPDNPzy1K4zW",
    "We Will Rock You": "4pbJqGIASGPr0ZpGpnWkDn",
    "Living on My Own": "2VCB1IOc2oLUkat0YCkTZ6",
    "The Great Pretender": "4RhkLF7D9fXIxnHNz1x77l",
    "Doing Alright": "6PT7wUJefYPEU1lX1lcLRJ",
    "Keep Yourself Alive": "3N25RDKNufh7Sz8v7fwtUP",
    "Seven Seas of Rhye": "0sRidOyZHABfl4GS3t4YXg",
    "Son and Daughter": "1zK7i2QyuCmpYE209BMcPZ",
    "Nevermore": "6n7zeRIrGj8hTFxNWGb9k1",
    "Father to Son": "4ODgFAlSa4RSeugPEXJGcQ",
    "Procession": "6Wh3qXoyxfK3KeZG1Hwyik",
    "Now I'm Here": "5v1osKVFv3rXWb1VJDO9pW",
    "Killer Queen": "4cIPLtg1avt2Jm3ne9S1zy",
    "Another One Bites The Dust": "5vdp5UmvTsnMEMESIF2Ym7",
    "Crazy Little Thing Called Love": "6xdLJrVj4vIXwhuG8TMopk",
    "Play the Game": "5p6xhgQCwzX0G9PadMU9GA",
    "Save Me": "1pBFEy8cz0Fq4Pru0c4awd",
    "I Want It All": "3Dpyn5Cu7BdURzo2ov4dku",
    "Rain Must Fall": "6jornLGJEzC3wFP2MFFvWg",
    "Scandal": "6ntpR3xo7Zcc9akHgcMbu5",
    "The Invisible Man": "6VoiY3rukFPoqzP4AoGPU8",
    "The Miracle": "5EQXJGm08LMM1ZtVmkYJMn",
    "Hammer to Fall": "7Im5F8fliiF16D2te5rYNv",
    "I Want to Break Free": "1MsBRSbt5dqJSw3RxXtvCM",
    "It's a Hard Life": "34MoKBRdC9JDjcL4b4X1Ic",
    "Radio Ga Ga": "1nQRg9q9uwALGzouOX5OyQ"
}

def create_playlist(sp, user_id, name, description, tracks):
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False, description=description)
    playlist_id = playlist['id']
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tracks)
    return playlist_id

def main():
    # Spotify API credentials
    CLIENT_ID = 'CLIENT_ID'
    CLIENT_SECRET = 'CLIENT_SECRET'
    REDIRECT_URI = 'http://localhost:8888/callback'
    USERNAME = 'USERNAME'
    SCOPE = 'playlist-modify-private'

    # Authenticate and create Spotify API object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE, username=USERNAME))

    # Read input text file
    with open(sys.argv[1], 'r') as file:
        playlist_prefix = file.readline().strip()
        lines = file.readlines()
    
    # Parse input text and create playlists
    playlists = {}
    outliers = []
    for line in lines:
        line = line.strip()
        if line:
            song_info = line.split('\t')
            if len(song_info) == 2:
                song_name, playlist_number = song_info
                playlist_name = f"{playlist_prefix} Cluster {playlist_number}"
                song_id = song_id_list.get(song_name)
                if song_id:
                    track_uri = f"spotify:track:{song_id}"
                    if playlist_name not in playlists:
                        playlists[playlist_name] = []
                    playlists[playlist_name].append(track_uri)
                else:
                    print("Parse error for song info.")
                    return 0
    
    # Create playlists
    playlist_links = {}
    for playlist_name, tracks in playlists.items():
        if len(tracks) > 1:
            # print(f"Creating playlist: " + playlist_name)
            playlist_id = create_playlist(sp, USERNAME, playlist_name, f'An Analysis Of Queen\'s Discography Using KMeans, DBScan, And Affinity Propagation Clustering Techniques Based On Full And Reduced Musical Feature Sets - by Earl Edison B. Felizardo & Josemaria Y. Layug III', tracks)
            playlist_links[playlist_name] = sp.playlist(playlist_id)['external_urls']['spotify']
        else:
            outliers += tracks

    # Create outliers playlist
    if outliers:        
        outliers_playlist_name = f"{playlist_prefix} Outliers"
        # print(f"Creating playlist: " + outliers_playlist_name)
        playlist_id = create_playlist(sp, USERNAME, outliers_playlist_name, f'An Analysis Of Queen\'s Discography Using KMeans, DBScan, And Affinity Propagation Clustering Techniques Based On Full And Reduced Musical Feature Sets - by Earl Edison B. Felizardo & Josemaria Y. Layug III', outliers)
        playlist_links[outliers_playlist_name] = sp.playlist(playlist_id)['external_urls']['spotify']

    # Print playlist links
    for name, link in playlist_links.items():
        print(f"{name}: {link}")

if __name__ == "__main__":
    main()