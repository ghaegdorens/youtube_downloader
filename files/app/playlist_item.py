import os
import youtube_dl
import shutil


class PlaylistItem:

    def __init__ (self, playlistItem, saveFormat, destinationDirectory, appConfig):
        self._playlistItem = playlistItem
        self._saveFormat = saveFormat
        self._destinationDirectory = destinationDirectory
        self._appConfig = appConfig
        

    @property
    def VideoUrl(self):
        url = 'https://www.youtube.com/watch?v={0}'.format(self._playlistItem['id'])
        print('VideoUrl: {0}'.format(url))
        return url

    @property
    def PlaylistDestinationDirectory(self):
        dir = os.path.join(self._destinationDirectory, \
                self._playlistItem['playlist'])

        if os.path.exists(dir) == False:
            os.mkdir(dir)
        
        print('PlaylistDestinationDirectory: {0}'.format(dir))
        return dir


    @property
    def VideoFullFilename(self):
        fullFilename = os.path.join(self.PlaylistDestinationDirectory, \
                self._playlistItem['title'] + '.' + self._saveFormat)
        print('VideoFullFilename: {0}'.format(fullFilename))
        return fullFilename


    def Download(self):
        try:
            print('id: {0}'.format(self._playlistItem['id']))
            print('playlist_id: {0}'.format(self._playlistItem['playlist_id']))
            print('uploader_id: {0}'.format(self._playlistItem['uploader_id']))
            print('uploader: {0}'.format(self._playlistItem['uploader']))
            print('video_title: {0}'.format(self._playlistItem['title']))

            if os.path.exists(self.VideoFullFilename):
                print("File already downloaded: {0}".format(self.VideoFullFilename))
            else:
                print("Download file: {0}".format(self.VideoFullFilename))
                
                self.download_from_youtube(self.VideoUrl, self._playlistItem['title'], self._saveFormat)
                self.move_file()

        except Exception as e:
            print("error occured in Playlist.GetYoutubePlaylistItems")
            print(e)


    def download_from_youtube(self, video_url, video_title, saveFormat):
        print("Downloading ... {0}".format(video_title))
    
        postprocessors = None
        if saveFormat == 'mp3':
            postprocessors = {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }
        elif saveFormat == 'mp4':
            postprocessors = {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }

        #Post processor list https://github.com/rg3/youtube-dl/blob/cc42941390b547ba950b4e76f4950be801f96134/youtube_dl/postprocessor/__init__.py#L25-L40
        outtmpl = video_title + '.%(ext)s'
        ydl_opts = {
            'username':self._appConfig.Youtube_username,
            'password':self._appConfig.Youtube_password,
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [
                postprocessors,
                {'key': 'FFmpegMetadata'},
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(video_url, download=True) 


    def move_file(self):
        for file in os.listdir("."):
            if file.endswith(self._saveFormat):
                video_filename = os.path.join(os.getcwd(),file)
                dest_filename = os.path.join(self.PlaylistDestinationDirectory,file)
                print('Move {0} to {1}'.format(file, dest_filename))
                shutil.move(video_filename, dest_filename)