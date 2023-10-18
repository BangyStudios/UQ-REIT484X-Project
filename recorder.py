import config

import pyaudio

class Recorder:
    def __init__(self):
        self.config = config.get_config()
        
        self.size_chunk = self.config.get("recorder").get("size_chunk")
        self.format = pyaudio.paInt16
        self.channels = self.config.get("recorder").get("channels")
        self.signal_sr = self.config.get("recorder").get("signal_sr")
        
        self.p = pyaudio.PyAudio()
        
    def open_stream(self):
        self.stream = self.p.open(format=self.format,
            channels=self.channels,
            rate=self.signal_sr,
            input=True,
            frames_per_buffer=self.size_chunk
        )
        
    def get_frames(self, length_segment=1):
        frames = list()
        for i in range(0, int(self.signal_sr / self.size_chunk * length_segment)):
            data = self.stream.read(self.size_chunk, )
            frames.append(data)

        return frames
        
    def close_stream(self):
        self.stream.close()
        
    def close(self):
        self.p.close()