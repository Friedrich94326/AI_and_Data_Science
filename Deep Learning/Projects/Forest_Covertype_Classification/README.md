## Problem Discription:
In this project, I use deep neural networks to predict forest cover type (the most common kind of tree cover) based only on \
cartographic variables. The actual forest cover type for a given 30 x 30 meter cell was determined from US Forest Service (USFS)\
Region 2 Resource Information System data. The covertypes are the following:
- Spruce/Fir
- Lodgepole Pine
- Ponderosa Pine
- Cottonwood/Willow
- Aspen
- Douglas-fir
- Krummholz

## Project Objectives:
- Develop one or more classifiers for this multi-class classification problem.
- Use TensorFlow with Keras to build my own classifier(s). 
- Use my knowledge of hyperparameter tuning to improve the performance of my model(s).
- Test and analyse performance.
- Create clean and modular code.

## Distribution of Covertypes:
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Deep%20Learning/Projects/Forest_Covertype_Classification/distribution%20of%20cover%20types.png)

## Architecture of Network:
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Deep%20Learning/Projects/Forest_Covertype_Classification/Trained_Models/covertype_3_layered_classifier/model_plot.png)

## Overview of Training History: Accuracy and Loss over Epochs:
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Deep%20Learning/Projects/Forest_Covertype_Classification/Outputs/acc_loss_plot.png)

## Performance of Our Classification Model:

### Confusion Matrix (Visualised through a Heatmap)
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Deep%20Learning/Projects/Forest_Covertype_Classification/Outputs/confusion_matrix.png)

### Scoring Our Model
![](https://github.com/Friedrich94326/AI_and_Data_Science/blob/Python/Deep%20Learning/Projects/Forest_Covertype_Classification/Trained_Models/covertype_3_layered_classifier/Model_Score.jpg)


## Dataset:
Data source: [Forest Cover Type Prediction](https://www.kaggle.com/c/forest-cover-type-prediction)
