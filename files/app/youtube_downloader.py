from app_config import AppConfig
from playlists import Playlists


def main():
    appConfig = AppConfig()
    playlists = Playlists(appConfig)
    playlists.Download()


if __name__ == '__main__':
    main()