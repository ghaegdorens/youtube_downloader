from playlist import *
import pandas as pd


class Playlists:
    def __init__(self, appConfig):
        self.appConfig = appConfig

        with open("../excluded/playlist.json", "r") as playlist_file:
            dfplaylist = pd.read_json(playlist_file.read(), orient='records')
            #print(dfplaylist)
    
        self._playlistItems = []

        for i, row in dfplaylist.iterrows():
            print("Getting items for '{0}'".format(row["playlist_name"]))
            
            playlistItem = Playlist(row["playlist_name"], row["playlist_id"], row["save_format"], appConfig)
            self._playlistItems.append(playlistItem)


    def Download(self):
        for playlistItem in self._playlistItems:
            playlistItem.Download()

            print("================================")
            print("================================")
            print("================================")


