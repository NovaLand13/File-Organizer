import os, shutil
from datetime import datetime

def organize_files(source_folder, pic_folder, destination_folder):
    PIC_FOLDER_EXTENSIONS = {'.jpg', '.mp4', '.mov', '.png'}
    DOC_EXTENSIONS = {'.pdf', '.doc','.docx', '.xlsx', '.pptx'}
   
    #loop through files 
    for filename in os.listdir(source_folder):    
        _, file_extention = os.path.splitext(filename)

        if file_extention.lower() in PIC_FOLDER_EXTENSIONS:
            pic_path = os.path.join(source_folder, filename)
            year_folder = create_folder(pic_path, pic_folder) 
            shutil.move(pic_path, os.path.join(year_folder, filename))

        if file_extention.lower() in DOC_EXTENSIONS:
            file_path = os.path.join(source_folder, filename)
            #if not os.path.isdir(file_path):
            year_folder = create_folder(file_path, destination_folder)  
            shutil.move(file_path, os.path.join(year_folder, filename))


def create_folder(file_path, source_folder):
    # Get files last mod date
    mod_time = os.path.getmtime(file_path)
    year = datetime.fromtimestamp(mod_time).year

    # Create folder for year
    year_folder = os.path.join(source_folder, str(year))
    if not os.path.exists(year_folder): 
        os.makedirs(year_folder)

    return year_folder

