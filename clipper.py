import os
from moviepy import VideoFileClip
import yt_dlp

# used to separate a clip into shorter subclips
def separate_movie(infile, outpath, starts, player):
    # 1) your source video
    video = VideoFileClip(infile)

    # 3) compute a matching list of end times by
    #    taking the next start, and for the last clip using video.duration
    ends = starts[1:] + [video.duration]

    # 4) loop and write out each subclip
    for idx, (t0, t1) in enumerate(zip(starts, ends), start=1):
        clip = video.subclipped(t0, t1)
        out_path = os.path.join(outpath, f"{player}_{idx:02d}.mp4")
        clip.write_videofile(out_path,
                            codec="libx264",
                            fps=video.fps,
                            audio=False,
                            logger=None)
        clip.close()

    video.close()

def download_1080p_video(url, output_path="./"):
    ydl_opts = {
        'format': 'best[height<=1080][ext=mp4]',  # Best quality up to 1080p, mp4 format
        'outtmpl': output_path + '%(title)s.%(ext)s',  # Output filename template
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Download completed!")
        except Exception as e:
            print(f"Error: {e}")

#Usage
# video_url = input("url>")
# download_1080p_video(video_url)

starts = [0, 2, 7, 13, 19, 21, 26, 30, 35, 41, 46, 51, 54, 58, 61, 66, 72, 75, 80, 85, 89, 93, 96, 100, 107, 112, 116]
inpath = os.path.join(os.getcwd(), "videos", "CURRY", "curryclipped.mp4")
outpath = os.path.join(os.getcwd(), "videos", "CURRY")
separate_movie(inpath, outpath, starts, "curry")