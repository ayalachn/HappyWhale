# HappyWhale

HappyWhale model implementation - Phase B

# User Documentation

## General Description

The purpose of our model is to accurately identify a dolphin or whale individual in a given image. 
Our model is implemented in Python (version 3.8.16) programming language, under the Pytorch framework (version 1.13.0+cu116) and GoogleColab is used as the platform to run our code.

# Steps to run HappyWhale desktop application

## Prequisitions:

1. Open Spyder (Python 3.9) 5.1.5 IDE

2. Inside Spider's terminal run the following line:

    pip install -r yolov5/requirements.txt

## Running Code
1. Open HappyWhaleApp.py in Spyder (Python 3.9) 5.1.5 IDE

2. Click run button inside IDE to open the HappyWhaleApp application

![Picture1](https://user-images.githubusercontent.com/81107065/213869369-d9b8caf8-15f9-4dc2-b18e-43928f878688.png)

3. Click “Upload” to choose a whale or dolphin image:

![Picture2](https://user-images.githubusercontent.com/81107065/213869546-a505f856-1043-445c-8234-fd8274e6cb84.png)

![Picture3](https://user-images.githubusercontent.com/81107065/213869547-28c4148d-ee8d-4f71-9bd7-2a2fb54d9e83.png)

4. Click “Detect” to find out the whale or dolphin individual ID:

![Picture4](https://user-images.githubusercontent.com/81107065/213869548-d3aadca7-5c82-42a1-a8d2-c3c90167e955.png)

5. Result:

![Picture5](https://user-images.githubusercontent.com/81107065/213869549-f8073cde-b7ab-4c95-b0a6-6b0acf9662c5.png)

# Steps to run HappyWhale model in GoogleColab

1. Unzip project, you should have the following files/directories:
 - HappyWhale.ipynb
 - YOLOv5
 - dataset

2. Inside your google drive, create a project directory with the following path: /content/gdrive/MyDrive/Final_Project/Phase_B.


If you wish to create a different path for the project, go to the HappyWhale.ipynb and change the following line inside the Config() class:

![Picture6](https://user-images.githubusercontent.com/81107065/213869531-c5ab8be9-8109-48e6-8c68-ce0fab8ddab6.png)


Make sure to change the project’s directory inside data.yaml (inside YOLOv5/data.yaml) to your personal directory path:

![Picture7](https://user-images.githubusercontent.com/81107065/213869535-b2da4818-e4cf-4c74-b66d-7b726982b2ca.png)

3. Create the following sub-folders inside the project directory in the following hierarchy:

![Picture8](https://user-images.githubusercontent.com/81107065/213869536-85bae9bc-6571-4dd2-b487-b188a4086e21.png)

Under the project directory, create two sub-directories: FinalCode, YOLOv5.
Under FinalCode, create five sub-directories: dataset, labeled_data, test, validation, train, yolov5_results.

4. Insert given files and directories under directories in google drive:
After creating directories and subdirectories (in previous step), insert the following files inside the directories you just made:

5. Inside
/content/gdrive/MyDrive/Final_Project/Phase_B/FinalCode/dataset insert images from given dataset directory. After this step, dataset directory in your google drive should look like this:

![Picture9](https://user-images.githubusercontent.com/81107065/213869538-c6c34e99-d894-4b54-9921-8f4defe8d352.png)

Inside /content/gdrive/MyDrive/Final_Project/Phase_B/YOLOv5 
insert files from the given YOLOv5 directory. After this step, YOLOv5 directory in your google drive should look like this:

![Picture10](https://user-images.githubusercontent.com/81107065/213869539-40ab5a08-3192-44c2-85ac-2da35d1cd4a8.png)

To train and test the HappyWhale model, open HappyWhale.ipynb in GoogleColab, and choose “run-all” in the Runtime tab.


# Configuring model’s hyperparameters

In order to change the model’s hyperparameters, go to the Config() class:

In order to change YOLOv5 hyperparameters, change the following values:

![Picture11](https://user-images.githubusercontent.com/81107065/213869542-96d77493-da14-4d10-8fb7-6c7064890e73.png)

In order to change ResNet50 hyperparameters, change the following values:

![Picture12](https://user-images.githubusercontent.com/81107065/213869544-7e099279-2238-4f56-837f-399e328300c7.png)


Note: After changing values inside Config(), be sure to run the class’ cell to update the model.


Results
Results of the HappyWhale model will be saved under labeled_data directory (/content/gdrive/MyDrive/Final_Project/Phase_B/FinalCode/labeled_data). 
Each prediction of the HappyWhale model is saved under labeled_data in the following manner:
labeled_data/predicted_whale_id/{all images that the model predicted to belong to this individual whale}.
