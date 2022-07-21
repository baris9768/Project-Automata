from moviepy.editor import *


text1 = "Sun Tzu said: In the operations\nof war, where there are in the field a\nthousand swift chariots, as many heavy\nchariots, and a hundred thousand mail-clad\nsoldiers, with provisions enough to carry them."

video = VideoFileClip("/Users/baris/Desktop/vscode_/DONE/assets/video1.mp4")

clip = video.subclip(0, 20)


text = TextClip(text1, font="Roboto", fontsize=35, color="yellow", bg_color="gray0", align="center")

text = text.set_position("center").set_duration(10)


last = CompositeVideoClip([clip, text])

last.write_videofile("./DONE/assets/video1_text.mp4")
last.close()
