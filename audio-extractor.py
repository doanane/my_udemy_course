# creating an audio extractor which yo can export the audio form a video and san=ve it in an MP3 format
import moviepy.editor as mp
import os
path = input("Enter the pat for the file video : \n")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")