from PIL import Image
from torch.utils.data import WeightedRandomSampler
import torch
import torchvision
import random
import os

class Dataset:
    def __init__(self):
        self.transform = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean=[0.5], std=[0.5]),
            torchvision.transforms.Grayscale()
        ])
        
    def get_ds(self, dataset_path):
        ds = torchvision.datasets.ImageFolder(root=dataset_path, transform=self.transform)
        return ds
        
    def get_dl_train(self, dataset_path, prop_train=0.75, size_batch=100, oversample=True):
        ds = torchvision.datasets.ImageFolder(root=dataset_path, transform=self.transform)
        class_to_idx = ds.class_to_idx
        
        n_train = int(prop_train * len(ds))
        n_test = len(ds) - n_train

        # Create splits
        ds_train, ds_test = torch.utils.data.random_split(ds, [n_train, n_test])
        
        # Setup sampler
        class_count = [0] * len(ds.classes)
        for _, index in ds_train:
            class_count[index] += 1

        weights = 1. / torch.tensor(class_count, dtype=torch.float)
        weights = weights / weights.sum()
        samples_weights = weights[ds_train.dataset.targets][ds_train.indices]
        print(weights)

        sampler = WeightedRandomSampler(samples_weights, len(samples_weights))

        # Create dataloaders
        dl_train = torch.utils.data.DataLoader(ds_train, batch_size=size_batch, shuffle=False, sampler=sampler) # sampler=sampler
        dl_test = torch.utils.data.DataLoader(ds_test, batch_size=size_batch, shuffle=False)
        
        return dl_train, dl_test, class_to_idx
    
    def get_dl_predict(self, dataset_path, size_batch=100):
        ds = torchvision.datasets.ImageFolder(root=dataset_path, transform=self.transform)
        dl = torch.utils.data.DataLoader(ds, batch_size=size_batch, shuffle=False)
        return dl
    
    def balance_subfolders(self, dataset_path):
        # Get a list of all subfolders
        subfolders = [f.path for f in os.scandir(dataset_path) if f.is_dir()]

        # Count the number of files in each subfolder and find the minimum count
        min_file_count = float('inf')
        for folder in subfolders:
            num_files = len([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
            min_file_count = min(min_file_count, num_files)

        # Randomly delete files in each subfolder to match the minimum file count
        for folder in subfolders:
            files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            random.shuffle(files)
            files_to_delete = files[min_file_count:]

            for file in files_to_delete:
                os.remove(os.path.join(folder, file))
    
class Transformer:
    def __init__(self):
        self.transform = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            # torchvision.transforms.Normalize(mean=[0.5], std=[0.5]),
            # torchvision.transforms.Grayscale()
        ])
    def get_transform_image(self, image_path):
        image = Image.open(image_path)
        return self.transform(image)
    def get_transform_numpy(self, segment):
        image = Image.fromarray(segment.astype('uint8'))
        return self.transform(image)