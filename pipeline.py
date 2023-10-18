import config
import dataset
import predict
import preprocessor
import recorder

import os
import shutil
import wave
import time
import requests

class Pipeline:
    def __init__(self):
        self.ds = dataset.Dataset()
        self.generator = preprocessor.Generator()

        self.exit = False
        
    def run(self):
        self.config = config.get_config()
        self.recorder = recorder.Recorder()
        self.predictor = predict.Predict()
        
        # Load configuration
        self.run_delay = self.config.get("pipeline").get("run_delay")
        self.update_freq = self.config.get("pipeline").get("update_freq")
        
        self.jetson_preprocess = self.config.get("offload").get("jetson_preprocess")
        
        self.path_recording = self.config.get("path").get("recording")
        self.path_recording_latest = os.path.join(self.path_recording, "latest.wav")
        self.path_recording_latest_generated = os.path.join(self.path_recording, "latest/")
        
        self.length_recording = self.config.get("recorder").get("length")
        
        # Create folders if not already exists
        self.init_folder(self.path_recording)
        self.init_folder(self.path_recording_latest_generated)
        
        class_last = None
        update_count = 0
        
        while True:
            if (self.exit):
                break
            
            # Save latest audio recording to temporary buffer file
            self.recorder.open_stream()
            frames = self.recorder.get_frames(self.length_recording)
            self.recorder.close_stream()
            with wave.open(self.path_recording_latest, 'wb') as outputFile:
                outputFile.setnchannels(self.recorder.channels)
                outputFile.setsampwidth(self.recorder.p.get_sample_size(self.recorder.format))
                outputFile.setframerate(self.recorder.signal_sr)
                outputFile.writeframes(b''.join(frames))
                
            # Load configuration
            length_segment = self.config.get("preprocessor").get("length_segment")
            size_batch = self.config.get("dataset").get("size_batch")
            
            # Delete existing recorded segments.
            self.clear_folder(self.path_recording_latest_generated)
            
            if self.jetson_preprocess:
                # Load configuration
                jetson_api_host = self.config.get("jetson").get("host")
                jetson_api_address = f"http://{jetson_api_host}"
                
                # Create folders if not already exists
                response = requests.get(f"{jetson_api_address}/api/jetson/init_folder", params={"path": self.path_recording})
                response = requests.get(f"{jetson_api_address}/api/jetson/init_folder", params={"path": self.path_recording_latest_generated})
                
                # Delete existing recorded segments.
                response = requests.get(f"{jetson_api_address}/api/jetson/clear_folder", params={"path": self.path_recording_latest_generated})
                
                with open(self.path_recording_latest, "rb") as file:
                    files = {"file": file}
                    data = {"path": self.path_recording}
                    response = requests.post(f"{jetson_api_address}/api/jetson/receive", files=files, data=data)
                    
                response = requests.get(f"{jetson_api_address}/api/jetson/preprocess")
            else:
                # Generate MFCCs
                self.generator.generate_features_to_images(self.path_recording_latest, self.path_recording_latest_generated, length_segment)
                
            # Generate dataloaders
            dl = self.ds.get_dl_predict(self.path_recording, size_batch)
            
            # Run prediction
            probabilities_dict = self.predictor.predict(dl)
            print(probabilities_dict)
            probabilities = list(probabilities_dict.values())
            
            class_current = max(probabilities_dict, key=probabilities_dict.get)
            
            # Check if the highest key has changed or n loops have passed
            if (class_last != class_current or update_count >= self.update_freq):
                # Reset loop counter
                update_count = 0

                # Update last_highest_key
                class_last = class_current
            
                # Upload probabilities to API server
                response = requests.post('http://localhost/api/add', json={'probabilities': probabilities})
                if (response.status_code == 201):
                    print('Probabilities inserted successfully')
                else:
                    print(f'Failed to insert probabilities: {response.json()}')
            
            update_count += 1
            
            # Delay for specified time
            time.sleep(self.run_delay)
        
    def init_folder(self, path_folder):
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)
            
    def clear_folder(self, path_folder):
        for input_file in os.listdir(path_folder):
            path_file = os.path.join(path_folder, input_file)
            try:
                if os.path.isfile(path_file):
                    os.unlink(path_file)
                elif os.path.isdir(path_file):
                    shutil.rmtree(path_file)
            except Exception as e:
                print(f'Failed to delete {path_file}. Reason: {e}')