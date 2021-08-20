from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
from pytube.cli import on_progress
import os

url = "https://www.youtube.com/playlist?list=PLfj7PB0WEpfF3sq72sWnf6k8yAC6xESHW"


def pls(url):
        
        playlist = Playlist(url)
        try:    
                title = playlist.title
                dir_path = os.getcwd()
                path = os.path.join(dir_path, title)
                os.mkdir(path)
                os.chdir(path)
                print("---------------------------------DOWNLOADING...-----------------------------\n")

                for video in playlist.videos:
                        try:
                                video.register_on_progress_callback(on_progress)
                                print("Downloading:",video.title)
                                video.streams.get_highest_resolution().download()
                                print("\n")
                        except Exception as exception:
                                print(f"Failed downloading:{video.title} | Error:{exception}")

                print("------------------------PLAYLIST DOWNLOAD COMPLETE--------------------------\n")
        except Exception as exception:
                print(f"Connection Error: {exception}")
pls(url)