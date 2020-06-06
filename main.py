


import glob
import os
import shutil


def move(src, dest,extension):
    contador = 0
    for file_path in glob.glob(os.path.join(src, '**', '*'+str(extension)), recursive=True):
        new_path = os.path.join(dest, os.path.basename(file_path))
        new_path = new_path.replace("."+str(extension)," - "+str(contador)+"."+str(extension))
        print ("" + file_path + " moved to " + new_path)
        contador = contador + 1
        shutil.move(file_path, new_path)
    return contador

def delete(src,extension):
    contador = 0
    for file_path in glob.glob(os.path.join(src, '**', '*'+str(extension)), recursive=True):
        os.chmod(file_path, 777)
        os.remove(file_path)
        print ("" + file_path + " deleted")
        contador = contador + 1
    return contador
    

#movidos = move("/Volumes/BRIAN/BCK/", "/Volumes/BRIAN/ALL/JPG/","jpeg")

deleted = delete("/Volumes/BRIAN/BCK/","HEIC")

print (str(deleted) + " files deleted")

