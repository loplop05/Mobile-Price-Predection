**Mobile Price Prediction 

A Machine Learning project that predicts the price range of mobile phones based on their hardware and software specifications using classification algorithms.

** Problem Statement

In the smartphone industry, pricing a mobile device correctly is very important. Mobile companies need to understand how different features such as RAM, battery power, camera quality, and screen resolution affect the final price of a device.

The goal of this project is to build a Machine Learning model capable of predicting the price category of a mobile phone using its specifications.

The target variable represents four different price ranges:

0 → Low Cost
1 → Medium Cost
2 → High Cost
3 → Very High Cost
🚀 Solution Overview

This project solves the problem using a complete Machine Learning workflow:

1️⃣ Data Collection

The dataset contains different mobile phone specifications such as:

Battery Power
RAM
Internal Memory
Camera Quality
Processor Speed
Screen Dimensions
Connectivity Features (3G, 4G, WiFi, Bluetooth)
Touch Screen Support
And more...
2️⃣ Data Preprocessing

Before training the model, the data was cleaned and prepared by:

Handling missing values
Renaming columns
Feature scaling
Splitting the dataset into training and testing sets
3️⃣ Exploratory Data Analysis (EDA)

EDA was performed to better understand:

Feature distributions
Correlations between variables
Important features affecting phone prices
Dataset patterns and trends
4️⃣ Model Building

Several Machine Learning classification algorithms were tested and compared, including:

Logistic Regression
Random Forest Classifier
K-Nearest Neighbors (KNN)
Support Vector Machine (SVM)

The models were trained on the dataset and evaluated using classification metrics.

5️⃣ Model Evaluation

The models were evaluated using:

Accuracy Score
Confusion Matrix
Classification Report

The best-performing model was selected based on prediction accuracy and overall performance.
