
"""Import libraries required by PyTorch"""
import torch
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, n_class):
        super(MLP, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.LazyLinear(out_features=512)
        self.fc2 = nn.LazyLinear(out_features=256)
        self.fc3 = nn.LazyLinear(out_features=n_class)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax()
        self.dropout = nn.Dropout()
        
    def forward(self, x):
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.softmax(self.fc3(x))
        return x
    
class CNN_Final(nn.Module):
    def __init__(self, n_class):
        super(CNN_Final, self).__init__()
        
        self.conv1 = nn.LazyConv2d(out_channels=10, kernel_size=2, stride=1)
        self.conv2 = nn.LazyConv2d(out_channels=60, kernel_size=2, stride=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.LazyLinear(out_features=1024)
        self.fc2 = nn.LazyLinear(out_features=n_class)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax()
        self.dropout = nn.Dropout()
        
    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = self.flatten(x)
        x = self.relu(self.dropout(self.fc1(x)))
        x = self.softmax(self.fc2(x))
        return x
    
class CNN(nn.Module):
    def __init__(self, n_class, conv1_params, conv2_params, fc1_out_features):
        super(CNN, self).__init__()
        
        self.conv1 = nn.LazyConv2d(**conv1_params)
        self.conv2 = nn.LazyConv2d(**conv2_params)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.LazyLinear(out_features=fc1_out_features)
        self.fc2 = nn.LazyLinear(out_features=n_class)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
        self.dropout = nn.Dropout()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = self.flatten(x)
        x = self.relu(self.dropout(self.fc1(x)))
        x = self.softmax(self.fc2(x))
        return x