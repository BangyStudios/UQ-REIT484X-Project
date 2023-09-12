import dataset
import predict
import preprocessor
import recorder

import wave
import asyncio
import requests

class Pipeline:
    def __init__(self):
        self.transformer = dataset.Transformer()
        self.predictor = predict.Predict()
        self.preprocessor = preprocessor.Generator()
        self.recorder = recorder.Recorder()
        
    async def run(self):
        while True:
            # Save latest audio recording to temporary buffer file
            frames = self.recorder.get_frames(length_segment=4)
            with wave.open("./buffer/latest.wav", 'wb') as outputFile:
                outputFile.setnchannels(self.recorder.channels)
                outputFile.setsampwidth(self.recorder.p.get_sample_size(self.recorder.format))
                outputFile.setframerate(self.recorder.signal_sr)
                outputFile.writeframes(b''.join(frames))
                
            # Generate MFCCs
            mfcc = self.preprocessor.generate_mfcc("./buffer/latest.wav", time_start=0, length_segment=2)
            mfcc_transformed = self.transformer.get_transform_numpy(mfcc)
            
            # Run prediction
            probabilities = self.predictor.predict(mfcc_transformed)[0]
            
            # Upload probabilities to API server
            response = requests.post('http://127.0.0.1/stats/add', json={'probabilities': probabilities})
            if response.status_code == 201:
                print('Probabilities inserted successfully')
            else:
                print(f'Failed to insert probabilities: {response.json()}')
            
            await asyncio.sleep(10)

pipeline = Pipeline()
asyncio.run(pipeline.run())