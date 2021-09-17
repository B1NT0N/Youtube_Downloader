from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import os

def single_audio(url):
        video=YouTube(url,on_progress_callback=on_progress)
        try:
                try:
                        dir_path = os.getcwd()
                        path = os.path.join(dir_path, "SDownloads")
                        os.mkdir(path)
                        os.chdir(path)
                except OSError:
                        os.chdir(path)
                        
                #video.register_on_progress_callback(on_progress)
                print("Downloading:",video.title)
                out_file = video.streams.filter(only_audio=True).first().download()
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                
                
        except Exception as exception:
                print(f"Failed downloading:{video.title} | Error:{exception}")
        os.chdir(dir_path)
         
def single_video(url):
        video=YouTube(url,on_progress_callback=on_progress)
        try:
                try:
                        dir_path = os.getcwd()
                        path = os.path.join(dir_path, "SVideo Downloads")
                        os.mkdir(path)
                        os.chdir(path)
                except OSError:
                        os.chdir(path)
                        
                #video.register_on_progress_callback(on_progress)
                print("Downloading:",video.title)
                video.streams.get_highest_resolution().download()

        except Exception as exception:
                print(f"Failed downloading:{video.title} | Error:{exception}")
        os.chdir(dir_path)  
              
def video_playlist(url):
        
        playlist = Playlist(url)
        
        try:
                try:    
                        title = playlist.title
                        dir_path = os.getcwd()
                        path = os.path.join(dir_path, title)
                        os.mkdir(path)
                        os.chdir(path)
                except:
                        os.chdir(path)
                print("---------------------------------DOWNLOADING...-----------------------------\n")
                count = 1
                for video in playlist.videos:
                        try:
                                video.register_on_progress_callback(on_progress)
                                print(f"Downloading({count}/{len(playlist.videos)}):{video.title}")
                                video.streams.get_highest_resolution().download()
                                print("\n")
                        except Exception as exception:
                                print(f"Failed downloading:{count}/{len(playlist.videos)}:{video.title} | Error:{exception}")
                        count=count+1
                print("------------------------PLAYLIST DOWNLOAD COMPLETE--------------------------\n")
                os.chdir(dir_path)
        except Exception as exception:
                print(f"Connection Error: {exception}")
                os.chdir(dir_path)

def audio_playlist(url):
        playlist = Playlist(url)
        try:    
                title = playlist.title
                dir_path = os.getcwd()
                path = os.path.join(dir_path, title)
                os.mkdir(path)
                os.chdir(path)
                print("---------------------------------DOWNLOADING...-----------------------------\n")
                count = 1
                for video in playlist.videos:
                        
                        try:
                                video.register_on_progress_callback(on_progress)
                                print(f"Downloading({count}/{len(playlist.videos)}):{video.title}")
                                out_file = video.streams.filter(only_audio=True).first().download()
                                base, ext = os.path.splitext(out_file)
                                new_file = base + '.mp3'
                                os.rename(out_file, new_file)
                                print("\n")
                        except Exception as exception:
                                print(f"Failed downloading:{video.title} | Error:{exception}")
                        count=count+1
                print("------------------------PLAYLIST DOWNLOAD COMPLETE--------------------------\n")
                os.chdir(dir_path)
        except Exception as exception:
                print(f"Connection Error: {exception}")
                os.chdir(dir_path)
                
if __name__ == "__main__":
	while True:
	                        
	        chc = input("\n================================\n             MENU            \n================================\n1 - Single Video\n2 - Video Playlist\n3 - Single Audio\n4 - Audio Playlist\n5 - Exit\n================================\nEnter a choice and press enter:")
	
	        if chc == "1":
	                url = input("Please Enter the URL:")
	                single_video(url)
	        elif chc == "2":
	                url = input("Please Enter the URL:")
	                video_playlist(url)
	        elif chc == "3":
	                url = input("Please Enter the URL:")
	                single_audio(url)
	        elif chc == "4":
	                url = input("Please Enter the URL:")
	                audio_playlist(url)
	        elif chc == "5":
	                print("Exiting...")
	                break 

        