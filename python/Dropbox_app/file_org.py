# import required modules 

import os
import shutil
# from pathlib import Path

# create a varible called path that takes the input of the directory to organize
path = input("Enter Path: ")
# create a variable called files consisting of a list of files 
files = os.listdir(path)
#  using for loop, we travel through every file, split the file name and extension of the files 
for file in files: 
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
# if the extension directory already exists move the file to that directory 
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
# if not make new directory and move the file into it 
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# print(files)




# source_path = Path(r"C:\Users\kmurp\OneDrive\Desktop\John Coding Bootcamp")



# print (path.exists)