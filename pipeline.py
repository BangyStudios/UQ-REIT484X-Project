import dataset
import predict
import preprocessor
import recorder

import wave

class Pipeline:
    def __init__(self):
        self.transformer = dataset.Transformer()
        self.predictor = predict.Predict()
        self.preprocessor = preprocessor.Generator()
        self.recorder = recorder.Recorder()
        
    def run(self):
        while(True):
            frames = self.recorder.get_frames()
            # Saving frames to temporary file
            with wave.open("./buffer/latest.wav", 'wb') as outputFile:
                outputFile.setnchannels(self.recorder.channels)
                outputFile.setsampwidth(self.recorder.p.get_sample_size(self.recorder.format))
                outputFile.setframerate(self.recorder.signal_sr)
                outputFile.writeframes(b''.join(frames))
                
            mfcc = self.preprocessor.generate_mfcc("./buffer/latest.wav", 0, 1)
            mfcc_transformed = self.transformer.get_transform_numpy(mfcc)
            print(self.predictor.predict(mfcc_transformed))
            
pipeline = Pipeline()
pipeline.run()