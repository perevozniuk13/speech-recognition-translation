from moviepy.editor import *
from getVideo import title 


#print(type(title))
#print(title, '.mp4')
#audioclip = AudioFileClip('{title}.mp4')
audioclip = AudioFileClip("the foolish rabbit  1 minute  Moral story in English  Short  story  for  kids l.mp4")
audioclip.write_audiofile("audio.wav")