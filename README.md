# HappyWhale
HappyWhale model implementation - Phase B

User Documentation
General Description
The purpose of our model is to accurately identify a dolphin or whale individual in a given image. 
Our model is implemented in Python (version 3.8.16) programming language, under the Pytorch framework (version 1.13.0+cu116) and GoogleColab is used as the platform to run our code.

# Steps to run HappyWhale desktop application

Prequisitions:

Open Spyder (Python 3.9) 5.1.5 IDE

Inside Spider's terminal run the following line:

pip install -r yolov5/requirements.txt

Open HappyWhaleApp.py in Spyder (Python 3.9) 5.1.5 IDE

Click run button inside IDE to open the HappyWhaleApp application

Click “Upload” to choose a whale or dolphin image:


Click “Detect” to find out the whale or dolphin individual ID:
Result:

Steps to run HappyWhale model in GoogleColab
Unzip project, you should have the following files/directories:
HappyWhale.ipynb
YOLOv5
dataset

Inside your google drive, create a project directory with the following path: /content/gdrive/MyDrive/Final_Project/Phase_B.

If you wish to create a different path for the project, go to the HappyWhale.ipynb and change the following line inside the Config() class:

Make sure to change the project’s directory inside data.yaml (inside YOLOv5/data.yaml) to your personal directory path:

Create the following sub-folders inside the project directory in the following hierarchy:

/content/gdrive/MyDrive/Final_Project/Phase_B/
|- FinalCode/
|	|-- dataset
|	|-- labeled_data
|	|-- test
|	|- validation
|	|-- train
|	|- yolov5_results
|- YOLOv5/
Under the project directory, create two sub-directories: FinalCode, YOLOv5.
Under FinalCode, create five sub-directories: dataset, labeled_data, test, validation, train, yolov5_results.

Insert given files and directories under directories in google drive:
After creating directories and subdirectories (in previous step), insert the following files inside the directories you just made:

Inside
/content/gdrive/MyDrive/Final_Project/Phase_B/FinalCode/dataset insert images from given dataset directory. After this step, dataset directory in your google drive should look like this:

Inside /content/gdrive/MyDrive/Final_Project/Phase_B/YOLOv5 
insert files from the given YOLOv5 directory. After this step, YOLOv5 directory in your google drive should look like this:


To train and test the HappyWhale model, open HappyWhale.ipynb in GoogleColab, and choose “run-all” in the Runtime tab.


Configuring model’s hyperparameters

In order to change the model’s hyperparameters, go to the Config() class:

In order to change YOLOv5 hyperparameters, change the following values:


In order to change ResNet50 hyperparameters, change the following values:

Note: After changing values inside Config(), be sure to run the class’ cell to update the model.


Results
Results of the HappyWhale model will be saved under labeled_data directory (/content/gdrive/MyDrive/Final_Project/Phase_B/FinalCode/labeled_data). 
Each prediction of the HappyWhale model is saved under labeled_data in the following manner:
labeled_data/predicted_whale_id/{all images that the model predicted to belong to this individual whale}.
