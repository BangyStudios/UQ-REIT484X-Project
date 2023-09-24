import torch
import torchaudio
import torchaudio.transforms as T
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

class Preprocessor():
    def __init__(self):
        self.coef_pe = 0.97
        self.frame_length = 0.025
        self.frame_hop = 0.010
        
        self.f_min = 200
        self.f_max = 8000
        
        self.n_filter = 26
        self.n_lfcc = 13
        self.n_mfcc = 13

    def get_preemphasis(self, segment):
        return T.Preemphasis()(segment)

    def get_mfcc(self, segment, segment_sr):
        mfcc = T.MFCC(
            sample_rate=segment_sr,
            n_mfcc=self.n_mfcc,
            # melkwargs={
            #     'n_fft': int(self.frame_length * segment_sr),
            #     'hop_length': int(self.frame_hop * segment_sr),
            #     'n_mels': self.n_filter,
            #     'center': False
            # }
        )(segment)
        
        return mfcc

    def get_lfcc(self, segment, segment_sr):
        lfcc = T.LFCC(
            sample_rate=segment_sr, 
            n_filter=self.n_filter,
            n_lfcc=self.n_lfcc
        )(segment)
        
        return lfcc

    def evaluate(self, segment, segment_sr):
        segment = self.get_preemphasis(segment)

        mfcc = self.get_mfcc(segment, segment_sr)
        lfcc = self.get_lfcc(segment, segment_sr)

        return mfcc, lfcc

class Generator():
    def __init__(self):
        self.preprocessor = Preprocessor()
        self.target_sr = 16000 # Target sampling rate

    def generate_features(self, signal, signal_sr, frame_offset, num_frames):
        """Generate MFCC and LFCC from a segment in an audio file"""
        segment = signal[:, frame_offset:(frame_offset+num_frames)]
        segment_sr = signal_sr
        mfcc, lfcc = self.preprocessor.evaluate(segment, segment_sr)
        return mfcc, lfcc

    def generate_features_to_images(self, input_file, output_folder, length_segment):
        """Generate feature images and save them to the output folder."""
        signal, signal_sr = torchaudio.load(input_file)
        signal = signal.mean(dim=0, keepdim=True) # Convert to mono
        signal = T.Resample(orig_freq=signal_sr, new_freq=self.target_sr)(signal) # Downsample
        signal_sr = self.target_sr
        
        length_total = (signal.shape[1] / signal_sr)
        filename = os.path.splitext(os.path.basename(input_file))[0]
        
        for i in np.arange(0, length_total, length_segment):
            time_start = i
            if (i + length_segment > length_total and (length_total - i) != length_segment):
                break

            frame_offset = int(time_start*signal_sr)
            num_frames = int(length_segment*signal_sr)
            
            mfcc, lfcc = self.generate_features(signal, signal_sr, frame_offset, num_frames)

            mfcc = mfcc.numpy()
            lfcc = lfcc.numpy()

            # Concatenate MFCC and LFCC
            mfcc_lfcc = np.hstack((mfcc, lfcc))

            # Normalize and save as image
            mfcc_lfcc_normalized = ((mfcc_lfcc - mfcc_lfcc.min()) / (mfcc_lfcc.max() - mfcc_lfcc.min()) * 255).astype(np.uint8)
            mfcc_lfcc_image = np.squeeze(mfcc_lfcc_normalized, axis=0)
            cv2.imwrite(os.path.join(output_folder, f"{filename}-{i:.3f}.png"), mfcc_lfcc_image)

    def generate_features_all(self, input_folder, length_segment=1):
        """Generate a dataset of datafiles of all audio files in the input folder"""
        for root, _, files in os.walk(input_folder):
            folder_current = os.path.basename(root)
            if root == input_folder or folder_current == "dataset":
                continue

            for filename in files:
                if filename == ".DS_Store":
                    continue
                input_file = os.path.join(root, filename)
                output_folder = os.path.join(input_folder, "dataset", folder_current)
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                self.generate_features_to_images(input_file, output_folder, length_segment)


def display(input_mfcc):
    print(input_mfcc.shape)
    # Assuming mfcc is a 2D numpy array of shape (num_frames, num_mfcc_coeffs)
    plt.imshow(input_mfcc, cmap='jet', aspect='auto')
    plt.xlabel('Frame index')
    # plt.ylabel('MFCC/LFCC coefficient index')
    plt.colorbar()
    plt.show()