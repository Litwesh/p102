import os 
import shutil
from_dir="D:\pex1"
to_dir="D:\Desktop\ex2"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention=="":
        continue
    if extention in ['.txt', '.doc', '.docx', '.pdf']  :
        path1=from_dir+'/'+file_name #d:destop/ex2/g1.png
        path2=to_dir+'/'+'image_files' #d:/ex1/images_files
        path3=to_dir+'/'+'image_files'+'/'+file_name #d:/ex1/images_files/g1.png
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3) 