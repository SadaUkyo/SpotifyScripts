# Spotify Scripts
Multiple scripts which use the Spotify Web API to achieve different tasks.

## LikedSongsLastXDays.py
This script looks at the songs you have added in the last x days (default is 30 days) and then adds them to a new playlist.

## CloneLikedSongs.py
This script clones your liked songs into a new playlist.

## Prerequisites
Before you can run the scripts, you need to register an application with Spotify. To do this, please follow the guide from Spotify: [Spotify guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app)

After registering the application, you will receive a client ID and a client secret. These credentials need to be added to the script. Additionally, both scripts contain a playlist ID which needs to be changed to the playlist you want to add the songs to. You can obtain the playlist ID from the link to the playlist.

The script requires Python 3 and the pip3 Spotipy package.

I strongly advise running this script on a machine with a graphical user interface (GUI) rather than a command-line interface (CLI), as it requires signing in to spotify.com in a web browser. Currently, there is no support for a fully automated setup.

