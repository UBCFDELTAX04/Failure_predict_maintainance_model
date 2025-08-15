⚙️ Predictive Maintenance Model
This repository contains a machine learning project that trains a predictive maintenance model to forecast potential machine failures based on sensor data. This project marks the first-ever model training at OCAC.

The model is built using a scikit-learn pipeline, which handles data preprocessing and model training in a single, consistent workflow. The final trained model is saved for easy deployment and future use without the need for retraining.

Project Structure:
predictive_maintenance.csv: The dataset used for training the model. It contains sensor readings and failure information.

predictive_maintenance_notebook.ipynb: (Assuming you save your Jupyter notebook with this name) The Jupyter Notebook containing the full step-by-step process of data loading, preprocessing, model training, evaluation, and saving.

requirements.txt: A list of all necessary Python libraries to run this project.

scaled_model.pkl: The final, saved machine learning pipeline. This file contains the trained model and its preprocessing steps.

app_maintainance_predictor.py: A Python script that loads the saved model and allows a user to input new data to get a real-time failure prediction.

Getting Started
To run this project on your local machine, follow these steps:

1. Clone the Repository
First, clone this repository to your local machine using Git:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies
Make sure you have Python and pip installed. Then, install all the required libraries using the requirements.txt file:

pip install -r requirements.txt

How to Use
Training the Model
The model is trained in the Jupyter Notebook. You can open and run the cells in maintenance_predictor.ipynb to see the entire process and recreate the scaled_model.pkl file.

Making Predictions
To make a new prediction using the saved model, you can run the app_maintainance_predictor.py script from your terminal:

python app_maintainance_predictor.py

The script will prompt you to enter the necessary sensor data (e.g., temperatures, speed, torque, and tool wear), and it will output a prediction of whether a failure is likely.

Technology Stack
Python: The core programming language.

pandas: For data manipulation and analysis.

scikit-learn: For the machine learning pipeline, including data preprocessing and the RandomForestClassifier model.

matplotlib & seaborn: For data visualization (e.g., the confusion matrix).

joblib: For saving and loading the trained model pipeline.
