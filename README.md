# Spotify Scripts

This repository contains multiple scripts which use the Spotify Web API to achieve different tasks.

## LikedSongsLastXDays.py

This script looks at the songs you have added in the last x days (default is 30 days) and then adds them to a new playlist.

## CloneLikedSongs.py

This script clones your liked songs into a new playlist.

## Prerequisites

Before you can run the scripts, you need to register an application with Spotify. To do this, please follow the guide from Spotify: [Spotify guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app)

After registering the application, you will receive a client ID and a client secret. These credentials need to be added to the `config.ini` file. Additionally, both scripts require a playlist ID which needs to be changed in the `config.ini` file to the playlist you want to add the songs to. You can obtain the playlist ID from the link to the playlist.

### Configuring the `config.ini` file

Create a file named `config.ini` in the same directory as the scripts. Here's how you should structure the `config.ini` file:

```ini
[Spotify]
client_id = your_client_id
client_secret = your_client_secret

[LikedSongsLastXDays]
playlist_id = your_playlist_id

[CloneLikedSongs]
playlist_id = your_playlist_id
```

### Running the Scripts

The script requires Python 3 and the spotipy package. Install the spotipy package using pip:

```bash
pip3 install spotipy
```

To run the scripts:

Ensure that you have configured the config.ini file with the correct credentials and playlist IDs.
Run the desired script using Python:

```bash
python3 LikedSongsLastXDays.py
```
```bash
python3 CloneLikedSongs.py
```
I strongly advise running these scripts on a machine with a graphical user interface (GUI) rather than a command-line interface (CLI), as they require signing in to spotify.com in a web browser. Currently, there is no support for a fully automated setup.
