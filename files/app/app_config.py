import json


class AppConfig:
    def __init__ (self):
        print("Read app.config")
    
        with open('../excluded/app.config.json', 'r') as fp:
            rDict = json.loads(fp.read())

            self._yt_username = rDict['emailaddress']
            self._yt_password = rDict['password']
            self._mp3_download_directory = rDict['mp3_download_directory']
            self._mp4_download_directory = rDict['mp4_download_directory']


    @property
    def Youtube_username(self):
        return self._yt_username


    @property
    def Youtube_password(self):
        return self._yt_password


    @property
    def Mp3_download_directory(self):
        return self._mp3_download_directory


    @property
    def Mp4_download_directory(self):
        return self._mp4_download_directory