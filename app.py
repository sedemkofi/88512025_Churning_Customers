# import tensorflow
from tensorflow.keras.models import load_model
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


st.write('by Sedem Amediku')
model = load_model('model.h5')

df = pd.read_csv('CustomerChurn_dataset.csv')

output_feature_values = st.empty()

# Features used for training
features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'PaymentMethod',
               'OnlineSecurity', 'TechSupport', 'InternetService']

#DataFrame with sample input for the app
input_data = pd.DataFrame(index=[0], columns=features)

st.sidebar.header('User Input Features')

import streamlit as st

# Input components for numerical features
tenure = st.sidebar.number_input('Enter Tenure', min_value=0, max_value=100, value=50)

monthly_charges = st.sidebar.number_input('Enter Monthly Charges', min_value=0, max_value=100, value=50)

total_charges = st.sidebar.number_input('Enter Total Charges', min_value=0, max_value=100000, value=50)

# Input components for categorical features
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])

online_security = st.sidebar.selectbox("Online Security", ["Yes", "No"])

contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two years"])

payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

tech_support = st.sidebar.selectbox("Tech Support",['No','Yes', 'No internet service'])

internet_service = st.sidebar.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
# Display the entered values
st.write("**Inputs**:")
st.write(f"Tenure: {tenure}")
st.write(f"Monthly Charges: {monthly_charges}")
st.write(f"Total Charges: {total_charges}")
st.write(f"Online Security: {online_security}")
st.write(f"Contract: {contract}")
st.write(f"Payment Method: {payment_method}")
st.write(f"Tech Support: {tech_support}")
st.write(f"Internet Service: {internet_service}")
# Add more write statements for other categorical features as needed

scaler = joblib.load('scaler.pkl')

if st.sidebar.button("Predict"):
    # Prepare the input data as a dictionary
    input_data = {
        'MonthlyCharges': monthly_charges,
        'tenure': tenure,
        'TotalCharges': total_charges,
        'Contract': contract,
        'PaymentMethod': payment_method,
        'OnlineSecurity': online_security,
        'TechSupport': tech_support,
        'InternetService': internet_service
    }
    input_df = pd.DataFrame([input_data])
    categorical_features = ['OnlineSecurity', 'Contract', 'PaymentMethod', 'TechSupport', 'InternetService']
    for column in categorical_features:
        input_df[column] = le.fit_transform(input_df[column])
    
    # print(input_df)
    scaled_input_data = scaler.transform(input_df)
    prediction = model.predict(scaled_input_data)[0]
    st.write('')
    st.write('**Prediction**')
    if prediction[0] > 0.5:
        st.write('The model predicts that the customer **will churn**  n .')
    else:
        st.write('The model predicts that the customer **will not churn**.')
        
    st.write("The model is 75% confident")




    