import modules

import torch
import torch.nn

from collections import deque

class Trainer():
    def __init__(self, path_state="./model.txt"):
        self.device = self.init_device(force_cpu=False) # Initialize device
        self.print_device()
        self.path_state = path_state
        try:
            self.model = torch.load(self.path_state)
        except(FileNotFoundError):
            self.model = modules.CNN(n_class=3).to(self.device)
        self.fn_optim = torch.optim.Adam(self.model.parameters(), lr=0.00005)
        self.fn_loss = torch.nn.CrossEntropyLoss()
        
    def train(self, dl_train, dl_test):
        # Train the model
        self.model.train()
        epoch = 0
        moving_accuracy = MovingAverage(window_size=5)
        while True:
            running_loss = 0.0
            for i, data in enumerate(dl_train, 0):
                X, y = data
                #print(X.dtype, X.shape)
                X, y = X.to(self.device), y.to(self.device)

                self.fn_optim.zero_grad()

                y_pred = self.model(X)
                loss = self.fn_loss(y_pred, y)
                loss.backward()
                self.fn_optim.step()

                running_loss += loss.item()
                
            running_loss = 0.0

            # Evaluate on test set and log results to TensorBoard
            correct = 0
            total = 0
            with torch.no_grad():
                for data in dl_test:
                    X, y = data
                    X, y = X.to(self.device), y.to(self.device)

                    y_pred = self.model(X)
                    _, predicted = torch.max(y_pred.data, 1)
                    total += y.size(0)
                    correct += (predicted == y).sum().item()

                accuracy = 100 * correct / total
                # writer.add_scalar('Test Accuracy', accuracy, epoch)
                print(f"[Test Accuracy | Epoch=[{epoch}] | {accuracy}]")
                
                if (moving_accuracy.get_average() >= 90):
                    break
                moving_accuracy.add(accuracy)
                epoch += 1
                
        torch.save(self.model, self.path_state)
        print("Saved model")
        # close the TensorBoard writer
        # writer.close()
        
    def init_device(self, force_cpu=False):
        if (force_cpu):
            return torch.device("cpu")
        
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
        
class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.data = deque(maxlen=window_size)
        self.avg = 0.0

    def add(self, value):
        if len(self.data) == self.window_size:
            self.avg -= self.data[0] / self.window_size
            self.data.popleft()
        self.data.append(value)
        self.avg += value / self.window_size

    def get_average(self):
        return self.avg