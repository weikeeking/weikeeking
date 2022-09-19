from pytube import YouTube
from moviepy.editor import *
import os
import sys

if len(sys.argv) != 2:
    sys.exit()

url = sys.argv[1]
video = YouTube(url)

mp4_file = video.streams.get_lowest_resolution().download()
mp3_file = f"{video.title}.mp3"

videoClip = VideoFileClip(mp4_file)
audioClip = videoClip.audio

audioClip.write_audiofile(mp3_file)

audioClip.close()
videoClip.close()

os.remove(mp4_file)