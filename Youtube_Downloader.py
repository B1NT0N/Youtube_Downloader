from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import os

url = "https://www.youtube.com/playlist?list=PLfj7PB0WEpfF3sq72sWnf6k8yAC6xESHW"

def sgl(url):
        video=YouTube(url)
        try:
                try:
                        dir_path = os.getcwd()
                        path = os.path.join(dir_path, "Downloads")
                        os.mkdir(path)
                        os.chdir(path)
                except OSError:
                        os.chdir(path)
                        
                video.register_on_progress_callback(on_progress)
                print("Downloading:",video.title)
                video.streams.get_highest_resolution().download()

        except Exception as exception:
                print(f"Failed downloading:{video.title} | Error:{exception}")
        os.chdir(dir_path)  
              
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
                os.chdir(dir_path)
        except Exception as exception:
                print(f"Connection Error: {exception}")
                os.chdir(dir_path)

chc = input("Select 1 for Single Video or 2 for Playlist (1/2): ")
if chc == "1":
        url = input("URL:")
        sgl(url)
elif chc == "2":
        url = input("URL:")
        pls(url)
        