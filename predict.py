import torch
import torch.nn
import numpy as np

class Predict:
    def __init__(self, path_state="./model.txt"):
        self.device = self.init_device() # Initialize device
        self.print_device()
        try:
            state = torch.load(path_state, map_location=self.device)
            self.model = state["model"].to(self.device)
            class_to_idx = state["class_to_idx"]
            self.idx_to_class = {v: k for k, v in class_to_idx.items()}
        except(FileNotFoundError):
            print(f"Model state file {path_state} not found.")
        
    def predict(self, dl):
        self.model.eval()
        predictions = []

        with torch.no_grad():
            for batch in dl:
                x = batch[0].to(self.device)
                y_pred = self.model(x)

                _, most_likely_classes = torch.max(y_pred, 1)
                predictions.extend(most_likely_classes.cpu().numpy())

        unique_elements, counts_elements = np.unique(predictions, return_counts=True)
        total_predictions = len(predictions)
        
        original_class_labels = self.idx_to_class
        probabilities = {original_class_label: 0.0 for original_class_label in original_class_labels.values()}
        for class_id, count in zip(unique_elements, counts_elements):
            original_class_label = original_class_labels[class_id]  # Convert to original class label
            probabilities[original_class_label] = count / total_predictions
        
        return probabilities
            
    def init_device(self):
        if (torch.backends.mps.is_available()):
            device = torch.device("mps")
        elif (torch.cuda.is_available()):
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")
        return device
    
    def print_device(self):
        """Prints the PyTorch device that is being used.
        """
        print(f"Device Selected = [{self.device}]")