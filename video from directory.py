import os 
import random


video_dir = 'Path_of_directory'
video = os.listdir(video_dir)
filename = random.choice(video)
path = os.path.join(video_dir, filename)
print(filename)
os.startfile(path)
    