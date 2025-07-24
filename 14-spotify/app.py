import os

from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Tus credenciales de Spotify
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

CLIENT_ID = "9b290c60526840139961210193aaf4ef"
CLIENT_SECRET = "757a1ba90e0b424a8e5d274bdfcf047b"

# Autenticación
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_top_tracks(limit=50):
    """
    Realiza una búsqueda general de canciones populares usando la API de búsqueda de Spotify.
    """
    query = "top"  # también puedes probar con "hits", "global top", etc.
    query = "year:2025 top hits"
    results = sp.search(q=query, type='track', limit=limit) # limit=50, market='ES')

    tracks = []
    for item in results['tracks']['items']:
        track = item
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'image': track['album']['images'][1]['url'] if track['album']['images'] else '',
            'preview_url': track['preview_url'],
            'spotify_url': track['external_urls']['spotify']
        })

    return tracks

@app.route('/')
def index():
    tracks = search_top_tracks(limit=50)
    return render_template('index.html', tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)

