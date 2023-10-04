import preprocessor
import dataset
import train
import config

import os
import time
import shutil

class Trainer:
    def __init__(self):
        self.config = config.get_config()
        
        self.generator = preprocessor.Generator()
        self.ds = dataset.Dataset()
        
    def generate_dataset(self):
        # Delete previously generated images
        try:
            shutil.rmtree(self.config.get("path").get("generated"))
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Generate images from files
        self.generator.generate_features_all(self.config.get("path").get("dataset"))
        
    def get_dataset(self):
        if self.config.get("dataset").get("balance_subfolders"):
            self.ds.balance_subfolders(self.config.get("path").get("generated"))
        dl_train, dl_test, class_to_idx = self.ds.get_dl_train(
            dataset_path=self.config.get("path").get("generated"), 
            prop_train=self.config.get("dataset").get("prop_train"), 
            size_batch=self.config.get("dataset").get("size_batch")
        )
        return dl_train, dl_test, class_to_idx
    
    def backup_state(self):
        try:
            path_state = self.config.get("path").get("state")
            path_states = self.config.get("path").get("states")
            
            # Fetch file creation time
            time_created = os.path.getctime(path_state)
            date_created = time.strftime('%Y%m%d-%H%M%S', time.localtime(time_created))

            # Create new file name
            path_state_backup = os.path.join(path_states, f"{date_created}.txt")

            # Rename file
            os.rename(path_state, path_state_backup)
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def run_train(self):
        self.generate_dataset()
        dl_train, dl_test, class_to_idx = self.get_dataset()
        self.backup_state()
        tr = train.Train()
        tr.train(dl_train, dl_test, class_to_idx)