import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from get_beatmaps import get_beatmaps

# authorize spotify api
spotify_cilent_id = os.environ['SPOTIFY_CLIENT_ID']
spotify_client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
spotify_redirect_url = 'http://localhost:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_cilent_id,
    client_secret=spotify_client_secret,
    redirect_uri=spotify_redirect_url,
    scope='playlist-modify-public'
))

# search songs id
beatmaps = get_beatmaps()
track_ids = []
type = 'track'
market = 'JP'
for beatmap in beatmaps:
    query = f'track:{beatmap[0]} artist:{beatmap[1]}'
    search_result = sp.search(q=query, type=type, market=market, limit=1)
    tracks = search_result['tracks']['items']
    if tracks:
        track_ids.append(tracks[0]['id'])
        print(f'track found! {beatmap[0]}')
    else: # if not found, loosen the search
        query = f'track:{beatmap[0]}'
        search_result = sp.search(q=query, type=type, market=market, limit=1)
        tracks = search_result['tracks']['items']
        if tracks:
            track_ids.append(tracks[0]['id'])
            print(f'track found! {beatmap[0]}')
        else:
            print(f'not found... {beatmap[0]}')

tracks_num = len(track_ids)
print(tracks_num)

# create playlist from id
playlist_name = "Your Osu! playlist"
playlist_description = "Created by Osu! to Spotify"
playlist = sp.user_playlist_create(user=sp.me()['id'], name=playlist_name, description=playlist_description, public=True)
batch_size = 100
for i in range(0, tracks_num, batch_size):
    batch_ids = track_ids[i:i+batch_size]
    sp.playlist_add_items(playlist_id=playlist['id'], items=batch_ids)
    
if track_ids:
    print(f'Success! Playlist created! {tracks_num} songs!')
else:
    print('No songs found on Spotify...')