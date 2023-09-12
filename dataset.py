from PIL import Image
from torch.utils.data import WeightedRandomSampler
import torch
import torchvision

class Dataset:
    def __init__(self, dataset_path, prop_train=0.75, size_batch=4, oversample=True):
        self.transform = torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean=[0.5], std=[0.5]),
            torchvision.transforms.Grayscale()
        ])
        self.dataset = torchvision.datasets.ImageFolder(root=dataset_path, transform=self.transform)
        print(self.dataset.classes)

        n_train = int(prop_train * len(self.dataset))
        n_test = len(self.dataset) - n_train

        self.dataset_train, self.dataset_test = torch.utils.data.random_split(self.dataset, [n_train, n_test])
        
        class_count = [0] * len(self.dataset.classes)
        for _, index in self.dataset_train:
            class_count[index] += 1

        weights = 1. / torch.tensor(class_count, dtype=torch.float)
        weights = weights / weights.sum()
        samples_weights = weights[self.dataset_train.dataset.targets][self.dataset_train.indices]
        print(weights)
        
        sampler = WeightedRandomSampler(samples_weights, len(samples_weights))

        self.dl_train = torch.utils.data.DataLoader(self.dataset_train, batch_size=size_batch, sampler=sampler, shuffle=False)
        self.dl_test = torch.utils.data.DataLoader(self.dataset_test, batch_size=size_batch, shuffle=False)
        
    def get_dl(self):
        return self.dl_train, self.dl_test
    
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