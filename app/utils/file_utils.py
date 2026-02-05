import os

def delete_temp_files(*file_paths):

    for path in file_paths:
        try:
            if os.path.exists(path):
                os.remove(path)
        except:
            pass


def validate_mp3_file(file_path):

    if not file_path.lower().endswith(".mp3"):
        raise ValueError("File must be MP3 format")
