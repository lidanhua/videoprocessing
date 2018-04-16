import moviepy.editor as mpy
import multiprocessing
import sys



# Function for cutting a video clip.

def cutvideo(a, b):
     video = mpy.VideoFileClip("%s.mp4" % a).subclip(b[0], b[1])
     return video.write_videofile("【%s】%s.mp4" % (a, b[2]))
     


# Function for translating the start and end point into number of seconds.

def translate(n):
     l = n.split(":")
     return (int(l[0]))*60 + int(l[1])


# Function for processing editted texts.
def processtxt(text):
     clip = text.split(", ", 2)
     clip[0], clip[1] = translate(clip[0]), translate(clip[1])
     clip[2] = clip[2].strip('\n')
     return clip

def processepisode(all_text):
     t = all_text
     i = 0
     e = t.index('\n', i)
     d = {}
     while e > -1:
          k = t[i].strip('\n')
          d[k] = t[i+1:e]
          i = e + 1
          if '\n' in t[i:]:
               e = t.index('\n', i)
          else:
               e = -1
     return d

# multiprocessing for faster video processing
if __name__=="__main__":
     file_object = open("Cut.txt") # Read the start, end point of and titles for clips.
     try:
          all_the_text = file_object.readlines()
     finally:
          file_object.close()
     Text = processepisode(all_the_text)
     for key in Text:
          for item in Text[key]:
               x = processtxt(item)
               p = multiprocessing.Process(target=cutvideo, args=(key, x))
               p.start()
               p.join()

