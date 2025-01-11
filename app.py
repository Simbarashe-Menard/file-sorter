import os
import shutil

print("""
######################################
##                                  ##
##                                  ##
##          Sorting Files           ##
##                                  ##
##                                  ##
######################################
      
""")

def list_files_recursive(path='.'):
    count = 0
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        file_name, file_ext = os.path.splitext(full_path)
        result = file_type(file_ext)
        new_path = os.path.join(path, result)
        if result != '':
            try:
                os.makedirs(new_path, exist_ok=True)
                shutil.move(full_path, new_path)
                count += 1
            except FileExistsError :
                print('File already exists!')
            except Exception as e :
                print(e)
    print('Done... \nMoved ' + str(count) + ' files')


def file_type(ext):

     # Define common Linux file type categories
    text_files = {".txt", ".md", ".log", ".csv", ".conf", ".ini", ".html"}
    scripts = {".sh", ".py", ".pl", ".rb", ".php"}
    images = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", "heic"}
    videos = {".mp4", ".mkv", ".avi", ".mov", ".flv"}
    audio = {".mp3", ".wav", ".ogg", ".flac"}
    compressed = {".zip", ".tar", ".gz", ".bz2", ".xz", ".7z"}
    executables = {".out", ".bin", ".run", ".appimage", ".deb"}
    documents = {".pdf", ".doc", ".docx", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"}


    if ext in text_files:
        return "Text"
    elif ext in scripts:
        return "Scripts"
    elif ext in images:
        return "Images"
    elif ext in videos:
        return "Videos"
    elif ext in audio:
        return "Audio"
    elif ext in compressed:
        return "Compressed"
    elif ext in executables:
        return "Executables"
    elif ext in documents:
        return "Document"
    else:
        return ""


directory_path = input('Enter directory... \n')
list_files_recursive(directory_path)