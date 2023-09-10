import pyaudio
import wave

class Recorder:
    def __init__(self):
        self.size_chunk = 4096
        self.format = pyaudio.paInt32
        self.channels = 2
        self.signal_sr = 44100
        self.length_segment = 2
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
            channels=self.channels,
            rate=self.signal_sr,
            input=True,
            frames_per_buffer=self.size_chunk
        )
        
    def get_frames(self):
        frames = list()
        for i in range(0, int(self.signal_sr / self.size_chunk * self.length_segment)):
            data = self.stream.read(self.size_chunk)
            frames.append(data)

        return frames
        
    def close(self):
        self.stream.close()
        self.p.terminate()