from moviepy.editor import *
import os

def text_add(text, video_path, start_time, end_time, duration, new_video_filename) -> None:
    """
    Autogenerate text clip.
    """
    video = VideoFileClip(video_path)
    clip = video.subclip(start_time, end_time)
    
    text1 = TextClip(text, font="Roboto", fontsize=35, color="yellow", bg_color="gray0", align="center")
    text1 = text1.set_position("center").set_duration(duration)

    last = CompositeVideoClip([clip, text1])
    last.write_videofile(new_video_filename)
    last.close()