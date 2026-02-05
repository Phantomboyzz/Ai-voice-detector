import os
from pydub import AudioSegment
import shutil

def save_temp_audio(file_path):
    return file_path


def convert_to_wav(mp3_path):
    wav_path = mp3_path.replace(".mp3", ".wav")

    shutil.copy(mp3_path, wav_path)

    return wav_path
