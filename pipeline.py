import dataset
import predict
import preprocessor
import recorder

import wave
import asyncio

class Pipeline:
    def __init__(self):
        self.transformer = dataset.Transformer()
        self.predictor = predict.Predict()
        self.preprocessor = preprocessor.Generator()
        self.recorder = recorder.Recorder()
        
    async def run(self):
        while True:
            # Save latest audio recording to temporary buffer file
            frames = self.recorder.get_frames(length_segment=2)
            with wave.open("./buffer/latest.wav", 'wb') as outputFile:
                outputFile.setnchannels(self.recorder.channels)
                outputFile.setsampwidth(self.recorder.p.get_sample_size(self.recorder.format))
                outputFile.setframerate(self.recorder.signal_sr)
                outputFile.writeframes(b''.join(frames))
                
            # Generate MFCCs
            mfccs = self.preprocessor.generate_features_to_images("./buffer/latest.wav", "./buffer/latest/", length_segment=0.5)
            
            # Generate dataloaders
            ds = dataset.Dataset()
            dl = ds.get_dl_predict("./buffer", size_batch=5)
            
            # Run prediction
            probabilities  = self.predictor.predict(dl)
            print(probabilities)
            
            # # Upload probabilities to API server
            # response = requests.post('http://192.168.0.223:5001/stats/add', json={'probabilities': probabilities})
            # if response.status_code == 201:
            #     print('Probabilities inserted successfully')
            # else:
            #     print(f'Failed to insert probabilities: {response.json()}')
            
            # await asyncio.sleep(10)

pipeline = Pipeline()
asyncio.run(pipeline.run())