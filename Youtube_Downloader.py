from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
from pytube.cli import on_progress

def progress_func(self,stream, chunk,file_handle, bytes_remaining):

    size = video.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)


def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

url = "https://www.youtube.com/playlist?list=PLKkk89TwM8FeRXdCudXzcpxlkCUpMqUAd"
playlist = Playlist(url)

print("---------------------------------DOWNLOADING...-----------------------------\n")

for video in playlist.videos:
	try:
		video.register_on_progress_callback(on_progress)
		print("Downloading:",video.title)
		video.streams.get_highest_resolution().download()
		print("\n")
	except:
		print("Failed downloading:",video.title)

print("------------------------PLAYLIST DOWNLOAD COMPLETE--------------------------\n")
