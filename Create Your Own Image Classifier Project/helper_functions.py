# Imports here
import time
import torch
import json
import pandas as pd
import numpy as np
from torch import nn
from PIL import Image
from torch import optim
import torchvision as tch
import matplotlib.pyplot as plt
import torchvision.datasets as ds
from collections import OrderedDict
import torchvision.transforms as tf
import torchvision.models as models
from read_transform_images import read_transform_images


def modify_nn(model_arch, num_classes):
    """Modifies the architecture of a trained network.

    Args:
        model_arch: trained model
        hidden_units: number of hidden units
        do_prob: drop out
        num_classes: number of classes

    Returns:
        model
    """
    
    if model_arch=='vgg16':
      model = models.vgg16(pretrained=True)
    if model_arch=='vgg13':
    	model = models.vgg13(pretrained=True)
    if model_arch=='densenet121':
    	model = models.densenet121(pretrained=True)
 
    for name, param in model.named_parameters():
        param.requires_grad=False

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
      
    clf = torch.nn.Sequential(OrderedDict([
                              ('fc1', nn.Linear(model.classifier[0].in_features, 2048)),
                              ('relu1', nn.ReLU()),
                              ('dropout1', nn.Dropout(p=0.2)),
                              ('fc2', nn.Linear(2048, 256)),
                              ('relu2', nn.ReLU()),
                              ('dropout2', nn.Dropout(p=0.2)),
                              ('fc3', nn.Linear(256, num_classes)),
                              ('output', nn.LogSoftmax(dim=1))
                              ]))
    model.classifier = clf
    model.to(device)
    return model

def save_checkpoint(model_arch, model, dataloaders, num_classes, optimizer, num_epochs, learning_rate, path='model_checkpoint.pth'):
    """Saves a model's checkpoint or state.
    
    Args:
    model: model whose checkpoint is to be saved
    optimizer: model optimizer
    path: path to save the checkpoint
    """
    checkpoint = {'model_arch': model_arch,
                  'classifier': model.classifier,
                  'num_classes': num_classes,
                  'model_state_dict': model.state_dict(),
                  'class_to_idx': dataloaders['train'].dataset.class_to_idx,
                  'optim_state_dict': optimizer.state_dict(),
                  'num_epochs': num_epochs,
                  'learning_rate':learning_rate
                 }
    torch.save(checkpoint, path)
    
    
def load_checkpoint(filepath):
    """Loads a saved model checkpoint.
    
    """
    checkpoint = torch.load(filepath)
    model = modify_nn(checkpoint['model_arch'], checkpoint['num_classes'])
    model.classifier = checkpoint['classifier']
    optimizer = optim.Adam(model.classifier.parameters(), lr=checkpoint['learning_rate'])
    model.load_state_dict(checkpoint.get('model_state_dict'))
    optimizer.load_state_dict(checkpoint.get('optim_state_dict'))
    model.class_to_idx = checkpoint.get('class_to_idx')
    
    return model, optimizer

def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    
    # TODO: Process a PIL image for use in a PyTorch model
    img = Image.open(image)
    n_mean = [0.485, 0.456, 0.406]
    n_std = [0.229, 0.224, 0.225]

    img.thumbnail(size=(256,256))

    width, height = 256, 256
    
    bottom = (height + 224)/2
    top = (height - 224)/2
    right = (width + 224)/2
    left = (width - 224)/2
   
    image = np.array(img.crop((left, top, right, bottom)))

    mean = np.array(n_mean)
    std = np.array(n_std)
    
    image=(image/255-mean)/std
    image= np.transpose(image, (2, 0, 1))
    
    return image

def predict(image_path, img_folder, model, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
     # TODO: Implement the code to predict the class from an image file

    dataloaders = read_transform_images(img_folder)

    model.class_to_idx = dataloaders['train'].dataset.class_to_idx
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    model.eval()
    image = process_image(image_path)
    image = torch.from_numpy(np.array([image])).float()
        
    with torch.no_grad():
        output = model.forward(image.to(device))
        ps = torch.exp(output)
    
        probs, classes = ps.topk(topk, dim=1)
    t_probs = probs.tolist()[0]
    t_classes = classes.cpu().numpy()[0].tolist()
    class_to_idx = model.class_to_idx
    idx_to_class = {value : key for key, value in class_to_idx.items()}
    t_classes = [idx_to_class[i] for i in t_classes]

    return t_probs, t_classes


def get_prediction_table(model, image_path, img_folder, topk, path_to_category_names):
    with open(path_to_category_names, 'r') as f:
        cat_to_name = json.load(f)
 
    probs, category_num = predict(image_path=image_path, img_folder=img_folder, model=model,
                                  topk=topk)

    category_name = list()
    for num in category_num:
        category_name.append(cat_to_name.get(str(num)))

    prediction_table = pd.DataFrame({"Name": category_name, "Probability": probs})

    return prediction_table


# TODO: Do validation on the test set

def testing(model, test_loader):
    test_loss = 0
    test_accuracy = 0
    criterion = nn.NLLLoss()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    
    model.to(device)
    model.eval()
    for inputs, labels in test_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        output = model.forward(inputs)
        loss = criterion(output, labels)
        
        test_loss += loss.item()
        
        ps = torch.exp(output)
        prob, classe = ps.topk(1, dim=1)
        equals = classe == labels.view(*classe.shape)
        test_accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

    return test_loss/len(test_loader), test_accuracy/len(test_loader)