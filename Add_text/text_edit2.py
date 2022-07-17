# Import everything needed to edit video clips 
from moviepy.editor import *
    
# loading video dsa gfg intro video 
clip = VideoFileClip("/Users/baris/Desktop/clip.mp4") 
    
# clipping of the video  
# getting video for only starting 10 seconds 
#clip = clip.subclip(0, 10)
    
# Reduce the audio volume (volume x 0.8) 
# clip = clip.volumex(0.8) 


text1 = "It is believed that the Unofficial Texinfo Format\nis in keeping with the spirit of the graciously\nfreely-distributed version."


txt_clip = TextClip(text1, fontsize = 35, color = 'yellow', font="Roboto", stroke_width=1.5, stroke_color="black")

txt_clip = txt_clip.set_pos('center').set_duration(20)
    

video = CompositeVideoClip([clip.subclip(0, 20), txt_clip]) 
    
video.write_videofile("clip_with_text.mp4")