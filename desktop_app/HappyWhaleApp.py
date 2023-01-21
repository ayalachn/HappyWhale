# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:12:32 2023

@author: AYALA & SHARON
"""

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import torch.nn as nn
import torch
import torchvision.models as models
import cv2

WEIGHTS_PATH = 'resnet50_weights.pth' # path to our trained resnet50 weights
YOLO_WEIGHTS = 'best.pt' # path to our trained YOLOv5 weights
device = torch.device('cpu') # running locally on CPU
img_filepath = ""
NUM_CLASSES = 14 # number of unique individuals in our dataset
ID_label = None
# whale and dolphin individual IDs in our dataset
class_names = ['027ac44f5b33', '02947a94c3fc', '02ac4e3ca497', '03095fb8bd05', '031816fd9d9d', '03880e5855cc', '03f3d1f0e58f', '04a9b1cad4d9', '255682316920', '281504409737', '320751707094', '345218493744', '541203120577', '617368452785']

# Load YOLOv5 model with our trained weights
yolo = torch.hub.load('ultralytics/yolov5', 'custom', path=YOLO_WEIGHTS) 


  
  
# This function will be called each time the "Upload" button is pressed    
def upload():
    global img_filepath
    global ID_label
    
    # delete previous runs
    import shutil
    import os
    
    directory = "cropped_image"
    
    if os.path.exists(directory):
      shutil.rmtree(directory)
      print(f"{directory} has been deleted.")
    else:
      print(f"{directory} does not exist.")
      
    # remove previous ID label
    if (ID_label != None):
        ID_label.destroy()
    
    
    # Open the file explorer and allow the user to select a JPG image
    img_filepath = filedialog.askopenfilename(title="Select image", filetypes=[("JPG files", "*.jpg")])
    if img_filepath:
        # Open the image and convert it to a PhotoImage object
        image = Image.open(img_filepath)
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
    
        # Update the label's image and position it in the center of the window
        image_label.config(image=image)
        image_label.image = image
        image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    else:
        messagebox.showinfo("No file selected", "No image file was selected")
    
    print(f"Selected file: {img_filepath}")
    
    
def load_model():
    global NUM_CLASSES # number of unique individuals in our dataset
    global WEIGHTS_PATH  # path to our trained resnet50 weights
    
    #Load the ResNet50 model from torchvision:
    model_ft = models.resnet50(pretrained=True) # we are using transfer learning in our mode, trained on ImageNET
    num_ftrs = model_ft.fc.in_features
    model_ft.avgpool = nn.AdaptiveAvgPool2d(1)
    model_ft.fc = nn.Linear(num_ftrs, NUM_CLASSES) # our fully connected layer that we previously trained
    
    # Load the model weights from the 'resnet50_weights.pth' file
    model_ft.load_state_dict(torch.load(WEIGHTS_PATH, map_location='cpu'))
    
    # Set the model to evaluation mode
    model_ft.eval()   
    
    return model_ft


# Load the ResNet50 model
resnet = load_model()

# Run YOLOv5 on image
def preprocess_img():
    global yolov5
    
    # Load the image
    image = cv2.imread(img_filepath) 
    
    results = yolo(image)  # Run YOLOv5 on image to find bounding boxes

    # Save cropped image according to bounding box
    crops = results.crop(save=True, save_dir='cropped_image')  # specify save dir
    

# Detect whale/dolphin individual
def detect():
    import torch
    import torchvision.transforms as transforms
    import torchvision.models as models
    
    global img_filepath
    global class_names
    global resnet
    global ID_label
    
    # Run YOLOv5 on image to get cropped image according to bounding box
    preprocess_img()
    
    # Open cropped image
    image = Image.open(r"cropped_image/crops/dolphin-whale/image0.jpg") 
    
    # Define the image transformations
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Apply the transformations
    image_tensor = transform(image).unsqueeze(0)
    
    # Run the image tensor through the ResNet50 model and get the output
    with torch.no_grad():
        output = resnet(image_tensor)
    
    # Get the predicted result
    _, predicted = torch.max(output, 1)
    
    # Create a label with the predicted result
    label = tk.Label(text=f"This is: {class_names[predicted[0]]}")

    # Add the label to the window
    label.pack()
    ID_label = label
    
# Create the main window
window = tk.Tk()
window.title("HappyWhale")
window.geometry("400x400+0+0")

# Set the window background image
background_image = Image.open("whale_background.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Create the "Upload" button
upload_button = tk.Button(text="Upload", command=upload)
upload_button.pack()

# Create the "Detect" button
detect_button = tk.Button(text="Detect", command=detect)
detect_button.pack()

# Run the main loop
window.mainloop()
