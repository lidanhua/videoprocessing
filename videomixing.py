# This is for mixing videos.
from moviepy.editor import *
import multiprocessing
import sys
import os 
import natsort # Librabry for correct order.

# Open and read files in wanted order.
curDir = os.getcwd()
clips = natsort.natsorted(os.listdir(curDir))

# Function for clips mixing.
def mixing(v):
    V = []
    for fn in v:
        if fn.endswith(".mp4"):
            V.append(VideoFileClip(fn))
    final_video = concatenate_videoclips(V)
    return final_video.write_videofile("")

# multiprocessing for faster video processing.
if __name__=="__main__":
    p = multiprocessing.Process(target=mixing, args=(clips,))
    p.start()
    p.join()
