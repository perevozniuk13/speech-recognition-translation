from pytube import YouTube

url = "https://youtu.be/bIDbiSUDOHQ"
video = YouTube(url)
video = video.streams.get_highest_resolution()
title = video.title
video.download()

#import requests 
#import m3u8
#import subprocess

#url = "blob:https://rezka.ag/14ca34f6-b47f-46ad-a11a-88b4cabc8ae4"
#r = requests.get(url)
#with open('video.mp4', 'wb') as f:
#    f.write(r.content)

#m3u8_master = m3u8.loads(r.text)
#print(type(m3u8_master))
#print(m3u8_master.data['playlists'])
#playlist_url = m3u8_master.data['playlists'][0]['uri']
#r = requests.get(playlist_url)
#playlist = m3u8.loads(r.text)

#with open("video.ts", "wb") as f:
#    for segment in playlist.data['segments']:
#        url = segment['url']
#        r = requests.get(url)
#        f.write(r.content)

#subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
