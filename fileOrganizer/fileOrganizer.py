import os, shutil
from datetime import datetime

def organize_files_by_year(source_folder):
    #loop through files 
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        

        #if not os.path.isdir(file_path):
        year_folder = create_folder(file_path, source_folder)                

        if verify_doc_type(filename):
            # Move file into folders
            shutil.move(file_path, os.path.join(year_folder, filename))


def verify_doc_type(filename):
    ALLOWED_EXTENSIONS = {'.pdf', '.doc','.docx', '.xlsx','.jpg'}
    _, file_extention = os.path.splitext(filename)
    # Return true if allowed
    return file_extention.lower() in ALLOWED_EXTENSIONS


def create_folder(file_path, source_folder):
    # Get files last mod date
    mod_time = os.path.getmtime(file_path)
    year = datetime.fromtimestamp(mod_time).year

    # Create folder for year
    year_folder = os.path.join(source_folder, str(year))
    if not os.path.exists(year_folder): return os.makedirs(year_folder)
    return year_folder



if __name__ == "__main__":
    # Specify folder to organize
    source_folder = r"C:/Users/marie/OneDrive/Documents/PythonTest/"
    organize_files_by_year(source_folder)


