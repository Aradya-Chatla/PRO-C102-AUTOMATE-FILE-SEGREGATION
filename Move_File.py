import os
import shutil

# Note: In my laptop it's Documents.
# Note: Change it if it's not in your device.
from_dir = "C:/Users/NAVIPET 13/Downloads"
to_dir = "C:/Users/NAVIPET 13/Documents"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == " ":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir +'/' + "documents"
        path3 = to_dir + '/' + "documents" + '/' + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + "....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving" + file_name + "....")
            shutil.move(path1, path3)