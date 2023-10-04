import dataset
import predict
import preprocessor
import recorder
import config as conf
import jetson_client

import os
import shutil
import wave
import time
import requests

class Pipeline:
    def __init__(self, run_delay=10):
        self.transformer = dataset.Transformer()
        self.predictor = predict.Predict()
        self.preprocessor = preprocessor.Generator()
        self.recorder = recorder.Recorder()
        self.config = conf.get_config()
        
        self.run_delay = run_delay
        self.exit = False
        
        self.recording_path = self.config.get("path").get("recording")
        self.latest_file = os.path.join(self.recording_path, "latest.wav")
        self.latest_path = os.path.join(self.recording_path, "latest/")
        
        self.size_batch = self.config.get("dataset").get("size_batch")
        self.jetson_predict = self.config.get("jetson").get("predict")
        
        # Create folders if not already exists
        self.init_folders()
        
    def run(self):
        while True:
            if (self.exit):
                break
            
            # Delete existing recorded segments.
            self.clear_folder(self.latest_path)
            
            # Save latest audio recording to temporary buffer file
            frames = self.recorder.get_frames(length_segment=self.run_delay)
            with wave.open(self.latest_file, 'wb') as outputFile:
                outputFile.setnchannels(self.recorder.channels)
                outputFile.setsampwidth(self.recorder.p.get_sample_size(self.recorder.format))
                outputFile.setframerate(self.recorder.signal_sr)
                outputFile.writeframes(b''.join(frames))
                
            # Generate MFCCs
            mfccs = self.preprocessor.generate_features_to_images(self.latest_file, self.latest_path, length_segment=0.5)
            
            if self.jetson_predict:
                probabilities_dict = jetson_client.send_command("predict")
                probabilities = list(probabilities_dict.values())
            else:
                # Generate dataloaders
                ds = dataset.Dataset()
                dl = ds.get_dl_predict(self.recording_path, size_batch=self.size_batch)
                
                # Run prediction
                probabilities_dict = self.predictor.predict(dl)
                probabilities = list(probabilities_dict.values())
            
            # # Upload probabilities to API server
            response = requests.post('http://localhost/api/add', json={'probabilities': probabilities})
            if response.status_code == 201:
                print('Probabilities inserted successfully')
            else:
                print(f'Failed to insert probabilities: {response.json()}')
            
            # Delay for specified time
            # time.sleep(self.run_delay)
        
    def init_folders(self):
        if not os.path.exists(self.recording_path):
            os.mkdir(self.recording_path)

        if not os.path.exists(self.latest_path):
            os.mkdir(self.latest_path)
            
    def clear_folder(self, input_folder):
        for input_file in os.listdir(input_folder):
            path_file = os.path.join(input_folder, input_file)
            try:
                if os.path.isfile(path_file):
                    os.unlink(path_file)
                elif os.path.isdir(path_file):
                    shutil.rmtree(path_file)
            except Exception as e:
                print(f'Failed to delete {path_file}. Reason: {e}')