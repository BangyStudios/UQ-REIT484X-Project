import librosa
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt
from PIL import Image
import os

class Preprocessor():
    """Constructor for signal"""
    def __init__(self):
        self.coef_pe = 0.95 # Pre-emphasis coefficient
        self.time_frame = 0.025 # Frame length in seconds
        self.time_step = 0.010 # Frame step in seconds
        self.n_cepstrum = 13 # Number of Cepstrum
        self.n_mel_freqs = 25 # Number of Mel freqency filters
        # self.n_lin_freqs = 25 # Number of linear frequency filters
        
    """0. Load the signal from a path with librosa"""
    def load_signal(self, signal_path):
        signal, signal_sr = librosa.load(signal_path)
        self.size_frame = int(round(self.time_frame * signal_sr / 2) * 2)
        self.size_step = int(round(self.time_step * signal_sr))
        return signal
    
    def load_segment(self, segment, segment_sr):
        self.signal_sr = segment_sr
        self.size_frame = int(round(self.time_frame * segment_sr / 2) * 2)
        self.size_step = int(round(self.time_step * segment_sr))
        signal = segment
        return signal
        
    """0.5. Apply bandpass filter"""
    def apply_bandpass(self, signal):
        nyquist = self.signal_sr / 2
        lower = 200
        upper = 8000
        b, a = scipy.signal.butter(4, [lower/nyquist, upper/nyquist], btype="band")
        signal = scipy.signal.filtfilt(b, a, signal)
        return signal
        
    """1. Return the pre-emphasized signal"""
    def get_preemphasis(self, signal):
        signal_pe = librosa.effects.preemphasis(signal, coef=self.coef_pe)
        return signal_pe

    """2. Return (overlapping) frames for a signal"""
    def get_frames(self, signal):
        frames = librosa.util.frame(signal, frame_length=self.size_frame, hop_length=self.size_step)
        return frames
    
    """3. Apply a hamming window to the frames"""
    def get_hamming(self, frames):
        window = np.hamming(self.size_frame) # Define hamming window
        frames = np.copy(frames) # Create a copy of frames
        frames *= window[:, np.newaxis] # Apply hamming window to frames
        frames_hamming = frames
        return frames_hamming
    
    """4. Calculate the fourier transform of the frames for spectrogram"""
    def get_ft(self, frames):
        self.ft = np.fft.rfft(frames, axis=0)
        power_spectrum = np.abs(self.ft) ** 2
        return power_spectrum
    
    """5. Apply Mel filterbank to the spectrogram"""
    def get_mel(self, spectrogram):
        self.mel_freqs = librosa.mel_frequencies(n_mels=self.n_mel_freqs, fmin=0, fmax=self.signal_sr/2)
        self.mel_filterbank = librosa.filters.mel(sr=self.signal_sr, n_fft=self.size_frame, n_mels=self.n_mel_freqs, fmin=0, fmax=self.signal_sr/2)
        spectrogram_mel = np.dot(self.mel_filterbank, spectrogram)
        return spectrogram_mel
    
    """6. Apply log compression to spectrogram (only for MFCC)"""
    def get_log(self, spectrogram):
        spectrogram_mel_log = np.log(np.maximum(spectrogram, 1e-10))
        return spectrogram_mel_log
    
    """7. Apply discrete cosine transform (DCT)"""
    def get_mfcc(self, spectrogram):
        mfcc = librosa.feature.mfcc(S=spectrogram, n_mfcc=self.n_cepstrum)
        return mfcc
    
    """Abstract function for getting values"""
    def evaluate(self, segment, segment_sr):
        signal = self.load_segment(segment, segment_sr)
        signal_pe = self.get_preemphasis(signal)
        frames = self.get_frames(signal_pe)
        frames_hamming = self.get_hamming(frames)
        power_spectrum = self.get_ft(frames_hamming)
        spectrogram_mel = self.get_mel(power_spectrum)
        spectrogram_mel_log = self.get_log(spectrogram_mel)
        mfcc = self.get_mfcc(spectrogram_mel_log)
        return mfcc
    
class Generator():
    def __init__(self):
        self.preprocessor = Preprocessor()
    
    def generate_mfcc(self, input_file, time_start, length_segment):
        """Generate a single MFCC image from a segment in an audio file"""
        segment, segment_sr = librosa.load(input_file, offset=time_start, duration=length_segment)
        mfcc = self.preprocessor.evaluate(segment, segment_sr)
        return mfcc
        
    def generate_mfccs(self, input_file, output_folder, length_segment):
        """Generate MFCC images and save them to the output folder."""
        length_total = librosa.get_duration(filename=input_file)
        X = list()
        filename = os.path.splitext(os.path.basename(input_file))[0]

        for i in range(0, int(length_total), length_segment):
            time_start = i
            mfcc = self.generate_mfcc(input_file, time_start, length_segment)
            X.append(mfcc)
            
            mfcc_normalized = ((mfcc - mfcc.min()) / (mfcc.max() - mfcc.min()) * 255).astype(np.uint8)
            mfcc_image = Image.fromarray(mfcc_normalized).convert("L")
            mfcc_image.save(os.path.join(output_folder, f"{filename}-{i}.png"))

        mfccs = np.stack(X)
        return mfccs

    def generate_mfccs_all(self, input_folder, length_segment=1):
        """Generate a dataset of datafiles of all audio files in the input folder"""
        for root, _, files in os.walk(input_folder):
            folder_current = os.path.basename(root)
            if (root == input_folder or folder_current == "dataset"): continue     
            for filename in files:
                input_file = os.path.join(root, filename)
                output_folder = os.path.join(input_folder, "dataset", folder_current)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                self.generate_mfccs(input_file, output_folder, length_segment)

def display(input_mfcc):
    print(input_mfcc.shape)
    # Assuming mfcc is a 2D numpy array of shape (num_frames, num_mfcc_coeffs)
    plt.imshow(input_mfcc, cmap='jet', aspect='auto')
    plt.xlabel('Frame index')
    # plt.ylabel('MFCC/LFCC coefficient index')
    plt.colorbar()
    plt.show()