#file to trim audio files
from moviepy import AudioFileClip
import os

#take a 10→20 sec clip
def get_audio_clip(audiopath, start_time, end_time):
    with AudioFileClip(audiopath) as af:
        clip = af.subclipped(start_time, end_time)
        clip.write_audiofile('tekitcut.mp3')

audiopath = os.path.join(os.getcwd(), "audio", "tekit.mp3")
get_audio_clip(audiopath, 0, 20)