import librosa
import numpy as np

def extract_audio_features(file_path):

    y, sr = librosa.load(file_path)

    pitch = librosa.yin(y, fmin=50, fmax=300)
    pitch_variance = float(np.var(pitch))

    spectral_flatness = float(
        np.mean(librosa.feature.spectral_flatness(y=y))
    )

    energy = float(np.mean(librosa.feature.rms(y=y)))

    return {
        "pitch_variance": pitch_variance,
        "spectral_flatness": spectral_flatness,
        "energy": energy
    }
