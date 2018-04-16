import moviepy.editor as mpy
import multiprocessing
import sys



# Function for cutting a video clip.

def cutvideo(a, b, c):
     video = mpy.VideoFileClip("第7集.mp4").subclip(a[0], a[1])
     return video.write_videofile("【第7集片段%s-%s】%s.mp4" % (b, c, a[2]))


# Function for translating the start and end point into number of seconds.

def translate(n):
     l = n.split(":")
     return (int(l[0]))*60 + int(l[1])


# Function for processing editing texts.
def processtxt(text):
     clip = text.split(", ", 2)
     clip[0], clip[1] = translate(clip[0]), translate(clip[1])
     clip[2] = clip[2].strip('\n')
     return clip


# multiprocessing for faster video processing
if __name__=="__main__":
     file_object = open("Cut.txt") # Read the start, end point of and titles for clips.
     try:
          all_the_text = file_object.readlines()
     finally:
          file_object.close()
     n = len(all_the_text)
     for item in all_the_text:
          m = all_the_text.index(item) + 1
          x = processtxt(item)
          p = multiprocessing.Process(target=cutvideo, args=(x, m, n))
          p.start()
          p.join()

