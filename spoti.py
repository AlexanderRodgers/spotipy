import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'disabledlasagna'

token = util.prompt_for_user_token(username, scope, client_id='4b045045feb449e3b6f607245206f83c', client_secret='f2d1ee8f9bbc4b7fb9e16e5af9adcf06', redirect_uri='http://spotify.com/')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)