from pytube import YouTube
from sys import argv

url = input('Enter URL: ')
#link = argv[1]
yt = YouTube(url)

print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("E:\youtubevideos")

print("completed")