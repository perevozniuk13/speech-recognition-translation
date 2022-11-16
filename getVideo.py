from pytube import YouTube

url = "https://youtu.be/bIDbiSUDOHQ"
video = YouTube(url)
video = video.streams.get_highest_resolution()
title = video.title
video.download()

