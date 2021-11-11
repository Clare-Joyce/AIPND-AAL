# Imports here
import numpy as np
import time
import torch
import matplotlib.pyplot as plt
import torchvision as tch
import torchvision.transforms as tf
import torchvision.datasets as ds
from collections import OrderedDict
from torch import nn
from torch import optim
from PIL import Image


# TODO: Define your transforms for the training, validation, and testing sets

"""
For the training, you'll want to apply transformations such as 
- random scaling, 
- cropping, and 
- flipping.

* Resized
* Normalize means and stds: 

Note: Normalize an tensor image with mean and standard deviation
"""

def read_transform_images(data_dir):

    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir = data_dir + '/test'
    
    n_mean = [0.485, 0.456, 0.406]
    n_std = [0.229, 0.224, 0.225]

    train_transform = tf.Compose([tf.RandomRotation(45),
                                  tf.RandomHorizontalFlip(),
                                  tf.RandomResizedCrop(224),
                                  tf.ToTensor(),
                                  tf.Normalize(n_mean, n_std)])

    validation_transform = tf.Compose([tf.Resize(256),
                                       tf.CenterCrop(224),
                                       tf.ToTensor(),
                                       tf.Normalize(n_mean, n_std)])

    test_transform = validation_transform

    # TODO: Load the datasets with ImageFolder
    train_dataset = ds.ImageFolder(train_dir, transform=train_transform)
    validation_dataset = ds.ImageFolder(valid_dir, transform=validation_transform)
    test_dataset = ds.ImageFolder(test_dir, transform=test_transform)

    img_datasets = {'train': train_dataset,
                    'validation': validation_dataset,
                    'test': test_dataset}

    # TODO: Using the image datasets and the trainforms, define the dataloaders
    trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
    validloader = torch.utils.data.DataLoader(validation_dataset, batch_size=32)
    testloader = torch.utils.data.DataLoader(test_dataset, batch_size=32)

    dataloaders =  {'train': trainloader,
                    'validation': validloader,
                    'test': testloader}
    return dataloaders
