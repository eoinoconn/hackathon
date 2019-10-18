import pprint
import sys
import os

import spotipy.spotipy as spotipy
import spotipy.spotipy.util as util


def play_sad():
    scope = 'streaming'
    username = "eoinoconn@gmail.com"
    token = util.prompt_for_user_token(username, scope)
    sad_uri = "https://open.spotify.com/track/3JOVTQ5h8HGFnDdp4VT3MP"
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.start_playback(uris=[sad_uri])

    else:
        print("Can't get token for", username)


def play_happy():
    scope = 'streaming'
    username = "eoinoconn@gmail.com"
    token = util.prompt_for_user_token(username, scope)
    happy_uri = "https://open.spotify.com/track/5b88tNINg4Q4nrRbrCXUmg"
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.start_playback(uris=[happy_uri])

    else:
        print("Can't get token for", username)

if __name__ == "__main__":
    play_sad()