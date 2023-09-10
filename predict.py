import torch
import torch.nn

class Predict:
    def __init__(self, path_state="./model.txt"):
        self.device = self.init_device() # Initialize device
        self.print_device()
        try:
            self.model = torch.load(path_state, map_location=self.device).to(self.device)
        except(FileNotFoundError):
            print(f"Model state file {path_state} not found.")
        
    def predict(self, x_sample):
        self.model.eval()
        with torch.no_grad():
            x = torch.tensor(x_sample).unsqueeze(1).to(self.device)
            y_pred = self.model(x)
            _, predicted = torch.max(y_pred.data, 1)
            predicted_label = predicted.item()
            
            # Map the predicted label back to original class label
            if self.classes:
                predicted_label = self.classes[predicted_label]
                
        return y_pred, predicted_label
            
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