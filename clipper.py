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

# WESTBROOK CLIPS

# starts = [0, 2, 5, 7, 12, 15, 20, 22, 26, 30, 35, 36, 40, 42, 45, 48, 52, 57, 58, 60, 64, 68, 73, 77, 80, 83, 87, 90]
# inpath = os.path.join(os.getcwd(), "videos", "WESTBROOK", "westbrook_clips.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "WESTBROOK")
# separate_movie(inpath, outpath, starts, "westbrook")

# DURANT CLIPS

# starts = [0, 4, 9, 14, 17, 21, 26, 29, 32, 38, 41, 44, 49, 56, 60, 66, 68, 72, 76, 82, 85, 94]
# inpath = os.path.join(os.getcwd(), "videos", "DURANT", "durant_clipped.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "DURANT")
# separate_movie(inpath, outpath, starts, "durant")

# starts = [0, 4, 7, 12, 17, 22, 27, 32, 36]
# inpath = os.path.join(os.getcwd(), "videos", "ASSIST", "assistclipped.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "ASSIST")
# separate_movie(inpath, outpath, starts, "assists")



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

# starts = [0, 7, 10, 12, 16, 19, 22, 26, 32, 35, 38, 41, 45, 49, 52, 55]
# inpath = os.path.join(os.getcwd(), "videos", "JAMES", "lebrondunks.mp4")
# outpath = os.path.join(os.getcwd(), "videos", "JAMES")
# separate_movie(inpath, outpath, starts, "lebrondunks")

starts = [0, 4, 12, 14, 16, 21, 26, 29]
inpath = os.path.join(os.getcwd(), "videos", "CELLY", "celly.mp4")
outpath = os.path.join(os.getcwd(), "videos", "CELLY")
separate_movie(inpath, outpath, starts, "celly")