# 88512025_Churning_Customers
Customer Churn Prediction App
This is a Streamlit web application for predicting customer churn. The app uses a machine learning model trained on customer data to predict whether a customer is likely to churn or not. It includes a user interface where users can input information about a customer, and the app will provide a prediction based on the trained model.

Getting Started
Prerequisites
Make sure you have the following dependencies installed:

Python 3.x
TensorFlow
pandas
scikit-learn
joblib
Streamlit
Install the required packages using:

bash
Copy code
pip install tensorflow pandas scikit-learn joblib streamlit
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/customer-churn-prediction-app.git
cd customer-churn-prediction-app
Run the Streamlit app:
bash
Copy code
streamlit run app.py
Open the provided URL in your web browser to access the application.
Input Features
The user can input the following features for prediction:

Tenure
Monthly Charges
Total Charges
Contract
Payment Method
Online Security
Tech Support
Internet Service
Predictions
Once the user inputs the required features and clicks on the "Predict" button, the app will display the model's prediction whether the customer will churn or not along with the confidence of the prediciton.

Model Information
The machine learning model is built using TensorFlow and saved as a .h5 file (model.h5). The preprocessing steps, such as scaling and label encoding, are stored in the scaler.pkl file.

Acknowledgments
The model was trained on the "Customer Churn" dataset.
The application is created by Sedem Amediku.

Link to model test:
https://github.com/sedemkofi/88512025_Churning_Customers/blob/1bc925d0d832f5630226600f2fd7e1d2debee656/Model%20Test.mp4
