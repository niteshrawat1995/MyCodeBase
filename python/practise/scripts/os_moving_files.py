import os
import shutil

os.chdir('/home/niteshrawat/Downloads')
down_dir = os.getcwd()
down_dir_list = os.listdir(down_dir)

dest_name = 'SACRED GAMES'
# os.path.join(down_dir,'SACRED GAMES')
if dest_name not in down_dir_list:
    os.mkdir(dest_name)

dest_path = os.path.join(down_dir, dest_name)

for f in down_dir_list:
    if f.startswith('Sacred.Games'):
        shutil.move(f, dest_path)
