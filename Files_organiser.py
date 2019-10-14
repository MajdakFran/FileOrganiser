import os
import shutil
import time
path = '/mnt/HDD/Downloads/Chrome/'
dest = '/mnt/HDD/Documents/Files/'
all_files = []


def file_extension(filename):
    return filename.split(".")[1]


while True:
    for i in os.walk(path):
        for fle in i:
            for fil in fle:
                if len(fil) > 1:
                    all_files.append(fil)

    for i in all_files:
        if os.path.exists(dest + file_extension(i)) == True and file_extension(i) != "crdownload":
            shutil.move(path + i, dest + file_extension(i))
        elif os.path.exists(dest + file_extension(i)) == False and file_extension(i) != "crdownload":
            os.mkdir(dest + file_extension(i))
            shutil.move(path + i, dest + file_extension(i))
    all_files = []
    time.sleep(20)
