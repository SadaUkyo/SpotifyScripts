# Spotifyscripts
Multiple scripts which use the Spotify web api to achieve diffrent things

# LikedSongsLastXDays.py
This skript looks at the songs which you have added in the last x days (default is 30 days) and then adds them to a new playlist.

# CloneLikedSongs.py
This skript clones your liked songs into a new playlist.

# Prequisits
Bevor you can run the scripts you need to register an application with spotify. To do this please follow the guide from Spotify:
[Spotify guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app)

From the application you get a client_id and a client_secret, both of which need to be added to the skript.
In both scripts there is a playlist id which needs to be changed to the playlist you want to add the songs. You can get the playlist it from the link to the playlist. 

The skript requieres python3 and the pip3 spotipy package. 

I strongly advise you to run this skript on a GUI based machine and not on a CLI only machine, because you need to sign in to spotify.com in a webbrowser. 
Currently there is no support for a fully automated setup. 
