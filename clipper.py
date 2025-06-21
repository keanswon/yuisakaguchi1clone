from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from moviepy import VideoFileClip

def download_file():

    url = input("URL >")
    folder = input("folder >")

    filepath = os.path.join(os.getcwd(), "videos", folder)

    yt = YouTube(url, on_progress_callback = on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    ys.download(filepath)

# used to separate a clip into shorter subclips
def separate_movie(infile, outpath, starts):
    # 1) your source video
    video = VideoFileClip(infile)

    # 3) compute a matching list of end times by
    #    taking the next start, and for the last clip using video.duration
    ends = starts[1:] + [video.duration]

    # 4) loop and write out each subclip
    for idx, (t0, t1) in enumerate(zip(starts, ends), start=1):
        clip = video.subclipped(t0, t1)
        out_path = os.path.join(outpath, f"curry_{idx:02d}.mp4")
        clip.write_videofile(out_path,
                            codec="libx264",
                            fps=video.fps,
                            audio=False,
                            logger=None)
        clip.close()

    video.close()

# LEBRON JAMES CLIPS
# starts = [0, 3, 6, 9, 12, 20, 25, 30, 37, 40, 46, 52, 57, 65, 71, 76, 78, 82, 88, 92]
# inpath = os.path.join(os.getcwd(), "videos", "LEBRON", "lebronclips.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "LEBRON")
# separate_movie(inpath, outpath, starts)

# CURRY CLIPS
# starts = [0, 5, 8, 13, 19, 25, 31, 34, 39, 44, 54, 60, 64, 69, 72, 78, 85, 88]
# inpath = os.path.join(os.getcwd(), "videos", "CURRY", "curryclipped.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "CURRY")
# separate_movie(inpath, outpath, starts)

download_file()