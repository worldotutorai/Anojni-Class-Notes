# os -operating system
import os
# mypath= 'D:\MY CLASSES\YAMUNA\Web Development\my ecommerce\style.css'

# # i have to check is the path exist
# print(os.path.exists(mypath))

# # its in list format
# # files= os.listdir(mypath)
# # for i in files:
# #     # i= style.css--- we give actual path
# #     print(os.path.split(i))

# # its separets the absolute path -- extension file
# # print(os.path.split(mypath)[1].split('.'))
   
# # separtes the filename and extension 
# print(os.path.splitext(mypath))

# import shutil
# source= 'D:\MY CLASSES\YAMUNA\Web Development\my ecommerce\index.html'
# # destination= 'D:\MY CLASSES\YAMUNA\Web Development\my ecommerce\copyfolder'
# # shutil.move(source,destination)
# # print("sucess")

# destination= 'D:\MY CLASSES\YAMUNA\Web Development\my ecommerce\yamuna.html'
# os.rename(source,destination)
# print("success")

# print(os.getcwd())  # current working dir 
# os.mkdir()
# os.makedirs('yamuna')

# dir="anju"
# parent_dir= r"D:\MY CLASSES\STUDENTS\Anju\filehandling"
# new_path= os.path.join(parent_dir,dir)
# os.makedirs(new_path)
# print("sucess")

# file="file1.txt"
# loc= r'D:\MY CLASSES\STUDENTS\Anju\filehandling\anju'
# path= os.path.join(loc,file)
# os.makedirs(path)

# will check


# os.remove(r'D:\MY CLASSES\STUDENTS\Anju\filehandling\anju\file1.txt')

# path=r'D:\MY CLASSES\STUDENTS\Anju\yamuna'
# os.rmdir(path)

# mac\\
# window reads // format -- r mode read the child nodes

# to handle file permisiions of metdata
# os.chmod()- change the file or dir permisiions
# os.chown() - change file owner and groupp(unix only)
# os.stat() -- 
# os.stat() # fetch the metdata like file size, permission, modifitction 

# set read write permisions for owner (0o600)
# os.chmod(r'D:\MY CLASSES\STUDENTS\Anju\filehandling\sample.txt',0o600)
# path=r'D:\MY CLASSES\STUDENTS\Anju\filehandling\sample.txt'
# f= open(path)
# print(f.read())


# # projects --- advance 
# import pathlib

# orgainse the files based on the file type 
import os, shutil
import time

# source= input(r"Enter the source folder path:  ")
# dest= input(r"Enter the destination folder to organise")

# '''
# path= r'C:\Users\Mamatha-Win10\Downloads\testing'
# for filename in os.listdir(path):
#     # print(filename)
#     # create a abs_path for the each filename
#     file_path= os.path.join(path,filename)
#     if os.path.isfile(file_path):
#         ext= os.path.splitext(file_path)[-1]
#         print(ext)
#         if "." not in ext:
#             print("No extesnion")
#         else:
#             organsied_folder= os.path.join(path,ext)
#             if os.path.exists(organsied_folder):
#                 print("folder already exist and files moved")
#                 time.sleep(0.5)
#                 shutil.move(file_path,organsied_folder)
#             else:
#                 os.mkdir(organsied_folder)
#                 print("organised folders created and files moved")
#                 time.sleep(0.5)
#                 shutil.move(file_path,organsied_folder)
    
#     else:
#         print("Path doesnt exist in the source folder")
# '''


# organise the files based on the date its created (modified) 
from datetime import datetime
# date files created 
# import datetime

final_time={}
folder = r"C:\Users\Mamatha-Win10\Downloads\Farah_ecommerce"
# source= os.chmod(r"C:\Users\Mamatha-Win10\Downloads\organised",mode=0o777)
dst= r'C:\Users\Mamatha-Win10\Downloads\testing'

# how orgainsed in the same folder -- based on file size  
# 
def orgainsed_by_date(folder):
    for filename in os.listdir(folder):
        file_path= os.path.join(folder,filename)
    
        # creation time
        timestamp= os.path.getmtime(file_path)
        date_created= datetime.fromtimestamp(timestamp)
        # print(date_created)

        hour= date_created.hour
        mints= date_created.minute

        time= float(str(hour)+ "."+ str(mints))

        final_time[time]=file_path

    
    # # print(sorted(final_time))
    time_sorted= sorted(list(final_time.keys()))
    print(time_sorted)
    sd = {i: final_time[i] for i in time_sorted}
    dst_path= sd.values()
    # print(dst_path)

    for i in dst_path:
        if os.path.exists(i):
            print("files exist and organised")
            shutil.copy(i,dst)
        else:
            # os.mkdirs(i)
            # shutil.move(folder,i)
            print("files not exist create dand  orgainsed")


orgainsed_by_date(folder)

# print(dir(datetime))
