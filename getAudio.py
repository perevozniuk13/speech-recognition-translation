from moviepy.editor import *
from getVideo import title


audioclip = AudioFileClip('{title}.mp4')
audioclip.write_audiofile("audio.wav")
