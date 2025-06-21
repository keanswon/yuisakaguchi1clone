# use moviepy to create the clip - take a video from videos folder, take in a caption, and create the movie with an audio

import os
from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from pathlib import Path
import random
import textwrap

FINAL_PATH = os.path.join(os.getcwd(), "FINAL", "reel.mp4")
AUDIO_FOLDER = os.path.join(os.getcwd(), "audio")
OUTPUT_PATH = os.path.join(os.getcwd(), "OUTPUT", "final.mp4")

# build your path
audiopath = os.path.join(os.getcwd(), 'audio', 'headlock_cut.mp3')
videopath = os.path.join(os.getcwd(), 'videos', 'LEBRON', 'LEBRONDUNK.mp4')

def annotate_video(
    video_path, audio_path, caption_text,
    output_path="output.mp4", font="Arial-Bold",
    font_size=54, margin_ratio=0.1,
    stroke_width=4, stroke_color="black"
):
    # Load video & audio inside context managers
    with VideoFileClip(video_path) as video, AudioFileClip(audio_path) as audio:
        # Prepare the text clip
        W, H = video.w, video.h
        inner_w = int(W * (1 - 2*margin_ratio))
        inner_h = int(H * (1 - 2*margin_ratio))

        # 1) stroke layer
        txt_stroke = (
            TextClip(
                text=caption_text,
                font=font,
                font_size=font_size,
                color="white",
                stroke_width=stroke_width,
                stroke_color=stroke_color,
                method="caption",
                size=(inner_w + 2*stroke_width, inner_h),
                text_align="center"
            )
            .with_duration(video.duration)
            .with_position(("center","center"))
        )

        final = CompositeVideoClip([video, txt_stroke]) \
                .with_audio(audio)
        
        # Trim to shortest
        target_dur = min(final.duration, audio.duration)
        final = final.subclipped(0, target_dur)

        # Write out
        final.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            fps=video.fps,
            logger=None
        )

        # Explicitly close the composite clip (which in turn closes its readers)
        final.close()

# takes random clips from the selected folder, concatonates them into a clip, then trims to 15 seconds
def grab_random_videos(folder):
    filepath = os.path.join(os.getcwd(), "videos", folder)
    print("Looking for folder:", filepath)
    print("Directory contents are:", os.listdir(filepath))
    if not os.path.exists(filepath):
        exit("invalid folder")
    
    p = Path(filepath)
    videos = [f for f in p.iterdir() if f.is_file()]
    random_clips = random.sample(videos, 5)

    clips = [VideoFileClip(c) for c in random_clips] # make everything a VideoFileClip
    final_clip = concatenate_videoclips(clips, method="compose")

    # hard coded to 20 because that's how long the audio length is
    final = final_clip.subclipped(0, 20)
    final.write_videofile(
        FINAL_PATH,
        codec="libx264",
        audio_codec="aac",
        fps=final_clip.fps,
        ffmpeg_params=["-crf", "18", "-preset", "slow"],
        logger=None
    )

    print("Videos Compiled")

# returns a random audio file, headlock and killshot weighed more
def grab_random_audio():
    audio_folder = Path(AUDIO_FOLDER)
    audio_files = [a for a in audio_folder.iterdir()]

    print("~~~~ Audio retrieved ~~~~")
    return random.choice(audio_files)

def wrap_caption(text, max_chars=40):
    # wrap at word boundaries, never mid‐word
    wrapper = textwrap.TextWrapper(
        width   = max_chars,
        break_long_words   = False,
        break_on_hyphens   = False
    )
    lines = wrapper.wrap(text)
    return "\n".join(lines)

def create_video():
    caption = input("caption>").replace("\\n", "\n")
    caption = wrap_caption(caption, 31)
    folder = input("folder>")
    grab_random_videos(folder) # puts our video in FINAL_PATH
    audio_path = grab_random_audio()
    annotate_video(FINAL_PATH, 
                   audio_path,  
                   font="/Users/ss/Library/Fonts/Roboto.ttf",
                   caption_text=caption,
                   output_path=OUTPUT_PATH
                )

# annotate_video(
#     video_path=videopath,
#     audio_path=audiopath,
#     font="/Users/ss/Library/Fonts/Roboto.ttf",
#     caption_text="when fine shyt texts first",
#     output_path="fineshyt.mp4"
# )

create_video()