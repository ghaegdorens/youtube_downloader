import youtube_dl
from playlist_item import PlaylistItem


class Playlist:

    def __init__ (self, playlistName, playlistId, saveFormat, appConfig):
        self._name = playlistName
        self._id = playlistId
        self._saveFormat = saveFormat
        self._appConfig = appConfig


    @property
    def Name(self):
        return self._name


    def GetDestinationDirectory(self):
        destinationDirectory = "R:\\temp\\"

        if self._saveFormat == 'mp3':
            destinationDirectory = self._appConfig.Mp3_download_directory
        elif self._saveFormat == 'mp4':
            destinationDirectory = self._appConfig.Mp4_download_directory

        print(destinationDirectory)

        return destinationDirectory

    
    def Download(self):
        print("Download playlist: '{0}'".format(self.Name))
        youtubePlaylistItems = self.GetYoutubePlaylistItems()
        self.DownloadYoutubePlaylist(youtubePlaylistItems)


    def GetYoutubePlaylistItems(self):
        result=None

        try:
            ydl_url = 'https://www.youtube.com/playlist?list={0}'.format(self._id)
            print('Getting List: {0}'.format(ydl_url))

            ydl_opts = {
                'username':self._appConfig.Youtube_username,
                'password':self._appConfig.Youtube_password
            }

            ydl = youtube_dl.YoutubeDL(ydl_opts)

            with ydl:
                result = ydl.extract_info(
                    ydl_url,
                    download=False # We just want to extract the info
                )
        except Exception as e:
            print("error occured in Playlist.GetYoutubePlaylistItems")
            print(e)

        return result


    def DownloadYoutubePlaylist(self, youtubePlaylistItems):
        try:
            for item in youtubePlaylistItems['entries']:
                playlistItem = PlaylistItem(item, self._saveFormat, self.GetDestinationDirectory(), \
                    self._appConfig)
                playlistItem.Download()

        except Exception as e:
            print("error occured in Playlist.GetYoutubePlaylistItems")
            print(e)

