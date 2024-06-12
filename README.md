# Introduction
#### This application makes a Spotify playlist from your played beatmap on *Osu!*.

# How to use
## Preparation
1. Install the required packages:
    ```bash
    $ pip install requests spotipy
    ```

1. Osu! API v2 Registration:
    - Login to your Osu! account.
    - Go to settings.
    - Add an OAuth application.
    - Copy your client ID and client secret.
    - Add the following environment variables:
        ```bash
        $ export OSU_CLIENT_ID="YOUR_CLIENT_ID"
        $ export OSU_CLIENT_SECRET="YOUR_CLIENT_SECRET"
        ```

1. Spotify API Registration:
    - Access the Spotify Developer Dashboard.
    - Create an app.
    - Set the redirect URI to "http://localhost:8888/callback".
    - Copy your client ID and client secret.
    - Add the following environment variables:
        ```bash
        $ export SPOTIFY_CLIENT_ID="YOUR_CLIENT_ID"
        $ export SPOTIFY_CLIENT_SECRET="YOUR_CLIENT_SECRET"
        ```

## Making a playlist
#### Run the script:
```bash
$ python3 main.py
```
Then go to your Spotify account to see the playlist!

# References
https://osu.ppy.sh/docs/index.html#introduction
https://spotipy.readthedocs.io/en/latest/#getting-started
https://developer.spotify.com/documentation/web-api/reference/search