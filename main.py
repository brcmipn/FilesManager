


import glob
import os
import shutil


def move(src, dest,extension):
    contador = 0
    for file_path in glob.glob(os.path.join(src, '**', '*'+str(extension)), recursive=True):
        new_path = os.path.join(dest, os.path.basename(file_path))
        new_path = new_path.replace("."+str(extension)," - "+str(contador)+"."+str(extension))
        print ("" + file_path + " - " + new_path)
        contador = contador + 1
        shutil.move(file_path, new_path)
    print (str(contador) + " archivos movidos")

move("/Volumes/BRIAN/BCK/", "/Volumes/BRIAN/ALL/JPG/","jpeg")