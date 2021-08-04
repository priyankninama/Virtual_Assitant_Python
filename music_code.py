import os 
import random


music_dir = 'Path_of_Directory'
songs = os.listdir(music_dir)
filename = random.choice(songs)
path = os.path.join(music_dir, filename)
print(filename)
os.startfile(path)
    