import modules
import config

import torch
import torch.nn
from collections import deque
import os
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt

class Train():
    def __init__(self):
        # Load configuration
        self.config = config.get_config()
        self.force_cpu = self.config.get("train").get("force_cpu")
        self.n_class = self.config.get("train").get("n_class")
        self.rate_learn = self.config.get("train").get("rate_learn")
        self.path_states = self.config.get("path").get("states")
        self.path_state = os.path.join(self.path_states, "latest.txt")
        self.cond_break = self.config.get("train").get("cond_break")
        self.accuracy_size = self.config.get("train").get("accuracy_size")
        self.accuracy_threshold = self.config.get("train").get("accuracy_threshold")
        self.n_epoch = self.config.get("train").get("n_epoch")
        self.best_for_threshold = self.config.get("train").get("best_for_threshold")
        
        self.device = self.init_device(force_cpu=self.force_cpu) # Initialize device
        self.print_device()
        self.init_model()
        
    def train(self, dl_train, dl_test, save=True, class_to_idx=None, model_params=None):
        # Train the model
        self.model.train()
        epoch = 0
        moving_accuracy = MovingAverage(window_size=self.accuracy_size)
        best_accuracy = 0
        best_for = 1
        accuracies = list()
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
                moving_accuracy.add(accuracy)
                if (accuracy > best_accuracy):
                    best_accuracy = accuracy
                    best_for = 0
                elif (accuracy != 0):
                    best_for += 1
                # writer.add_scalar('Test Accuracy', accuracy, epoch)
                accuracies.append(accuracy)
                print(f"[Test Accuracy | Epoch=[{epoch}] | {accuracy}]")
                
                if (self.cond_break == "moving_accuracy"):
                    if (moving_accuracy.get_average() >= self.accuracy_threshold):
                        break
                elif (self.cond_break == "n_epoch"):
                    if (epoch > self.n_epoch):
                        break
                elif (self.cond_break == "best_for"):
                    if (best_for >= self.best_for_threshold):
                        break
                
                epoch += 1
        
        if (save):
            state = {
            'model': self.model,
            'class_to_idx': class_to_idx
            }   
            
            if not os.path.exists(self.path_states):
                os.makedirs(self.path_states)
            
            torch.save(state, self.path_state)
            print("Saved model")
            
        plt.plot(range(len(accuracies)), accuracies)
        plt.xlabel("Epochs")
        plt.ylabel("Accuracy")
        plt.title("Validation Accuracy")
        plt.show()
        
        # close the TensorBoard writer
        # writer.close()
        
        return moving_accuracy.get_average()
        
    def train_kfcv(self, ds, size_batch, k, model_params):
        kf = KFold(n_splits=k, shuffle=True, random_state=42)
        accuracies = list()
        fold = 1
        
        for idx_train, idx_test in kf.split(ds):
            subsampler_train = torch.utils.data.SubsetRandomSampler(idx_train)
            subsampler_test = torch.utils.data.SubsetRandomSampler(idx_test)
            
            dl_train = torch.utils.data.DataLoader(ds, sampler=subsampler_train, batch_size=size_batch)
            dl_test = torch.utils.data.DataLoader(ds, sampler=subsampler_test, batch_size=size_batch)
            
            self.init_model(model_params)
            
            accuracy = self.train(
                dl_train=dl_train, 
                dl_test=dl_test, 
                save=False, 
            )
            accuracies.append(accuracy)
            print(f"[Test Accuracy | Fold=[{fold}/{k}] | {accuracy}]")
            fold += 1
            
        return sum(accuracies) / len(accuracies)
        
    def init_device(self, force_cpu=False):
        if (force_cpu):
            return torch.device("cpu")
        try:
            if (torch.backends.mps.is_available()):
                device = torch.device("mps")
            elif (torch.cuda.is_available()):
                device = torch.device("cuda")
            else:
                device = torch.device("cpu")
        except (AttributeError):
            device = torch.device("cpu")
        return device
    
    def print_device(self):
        """Prints the PyTorch device that is being used.
        """
        print(f"Device Selected = [{self.device}]")
        
    def init_model(self, model_params=None):
        try:
            self.model = torch.load(self.path_state)
        except(FileNotFoundError):
            if (model_params == None):
                self.model = modules.CNN_Final(n_class=self.n_class).to(self.device)
            else:
                self.model = modules.CNN(**model_params).to(self.device)
        self.fn_optim = torch.optim.Adam(self.model.parameters(), lr=self.rate_learn)
        self.fn_loss = torch.nn.CrossEntropyLoss()
        
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