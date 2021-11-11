import numpy as np
import pandas as pd
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
import read_transform_images
import helper_functions
from read_transform_images import read_transform_images

parser = argparse.ArgumentParser()

parser.add_argument('--model_arch', default="vgg16")
parser.add_argument('img_path', default='./flowers/test/100/image_07896.jpg', type=str)
parser.add_argument('checkpoint', default='./model_checkpoint.pth', type=str)
parser.add_argument('--topk', default=5, type=int)
parser.add_argument('--category_names', default='cat_to_name.json')
parser.add_argument('--lr', type=float,default=0.001)
parser.add_argument('--data_dir', default="./flowers/", type=str)

args = parser.parse_args()


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model, optimizer = helper_functions.load_checkpoint(args.checkpoint)
    model.to(device)
        
    df = helper_functions.get_prediction_table(model, args.img_path, args.data_dir, args.topk, args.category_names)
    print(df)

    
if __name__== "__main__":
    main()