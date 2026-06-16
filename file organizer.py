import os
import shutil

#folder path  you want to organize
folder_path=os.getcwd() #current working directory

# file types and their corresponding folders
file_types={
    'Images':['.jpg','.jpeg','.png','.gif','.bmp'],
    'Documents':['.pdf','.doc','.docx','.txt','.xls','.xlsx','.ppt','.pptx'],
    'Videos':['.mp4','.avi','.mkv'],
    'Audio':['.mp3','.wav','.flac'],
    'Archives':['.zip','.rar','.tar','.gz'],

}
# create folders if they don't exist
for folder in file_types.keys():
    folder_dir=os.path.join(folder_path,folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

# organize files in the folder
for filename in os.listdir(folder_path):
    file_path=os.path.join(folder_path,filename)
    if os.path.isfile(file_path):
        ext=os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                shutil.move(file_path, os.path.join(folder_path,folder,filename))
                break
            
