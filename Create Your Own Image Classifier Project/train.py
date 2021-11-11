import numpy as np
import argparse
import torch
from torch import nn, optim
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models

from collections import OrderedDict
import matplotlib.pyplot as plt
import json
from PIL import Image
from read_transform_images import read_transform_images

import helper_functions

parser = argparse.ArgumentParser()
parser.add_argument('--model_arch', default="vgg16", type=str)
parser.add_argument('data_dir', default="./flowers/", type=str)
parser.add_argument('--lr', type=float,default=0.001)
parser.add_argument('--num_classes', type=int, default=102)
parser.add_argument('--dropout',type=float, default=0.2)
parser.add_argument('--checkpoint', default="./model_checkpoint.pth")
parser.add_argument('--num_epochs', default=4, type=int)
args = parser.parse_args()

def retrain_model(model, epochs, dataloaders, learning_rate):

    i = 0 
    training_loss = 0 
    print_every_n = 10 
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), lr=learning_rate)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device)

    for epoch in range(epochs):
        model.train()    # Activate training mode
        for inputs, labels in iter(dataloaders['train']):
            i += 1
            
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            
            outputs = model.forward(inputs)
            loss = criterion(outputs, labels)
            
            loss.backward() 
            optimizer.step()
            
            training_loss += loss.item() # Record the training loss

            if i % print_every_n == 0:
                model.eval()    
                # No backward propagation and optimization during validation
                validation_accuracy = 0
                validation_loss = 0
                with torch.no_grad():
                    for inputs, labels in iter(dataloaders['validation']):
                        inputs, labels = inputs.to(device), labels.to(device)
                        
                        output = model.forward(inputs)
                        validation_loss += criterion(output, labels).item()
                        
                        ps = torch.exp(output)
                        prob, classe = ps.topk(1, dim=1)
                        equals = classe == labels.view(*classe.shape)
                        validation_accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                    print(f"Epoch: {epoch+1}/{epochs}\n"
                          f"Training Loss: {(training_loss / print_every_n):.2f}\n"
                          f"Validation Loss: {(validation_loss / len(dataloaders['validation'])):.2f} \n"
                          f"Validation Accuracy: {(validation_accuracy / len(dataloaders['validation'])):.2f}\n")

                # Reset training loss
                training_loss = 0
                # Activate training mode
                model.train()
    return model, optimizer

def main():
    dataloaders = read_transform_images(args.data_dir)
    model = helper_functions.modify_nn(args.model_arch, num_classes=args.num_classes)

    model, optimizer = retrain_model(model, args.num_epochs, dataloaders, args.lr)
   
    helper_functions.save_checkpoint(model_arch=args.model_arch, model=model, dataloaders=dataloaders,
                                     num_classes=args.num_classes, optimizer=optimizer,
                                     num_epochs=args.num_epochs, learning_rate=args.lr, path=args.checkpoint)
    test_loss, test_accuracy = helper_functions.testing(model, dataloaders['test'])
    print(f"Test Loss: {test_loss:.2f}\n"
          f"Test accuracy: {100*test_accuracy:.2f}")

if __name__ == "__main__":
    main()