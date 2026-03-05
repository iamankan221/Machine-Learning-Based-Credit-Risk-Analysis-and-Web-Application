import streamlit as st
import pandas as pd
import joblib

# Load model
try:
    model = joblib.load('extra_trees_credit_model.pkl')
except:
    st.error("Model file not found.")
    st.stop()

# Load encoders
encoders = {
    col: joblib.load(f'{col}_encoder.pkl')
    for col in ['Sex','Housing','Saving accounts','Checking account','Purpose']
}

st.title("Credit Risk Prediction App")
st.write("Enter the application information to predict credit risk.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", ['male', 'female'])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ['own', 'rent', 'free'])
saving_accounts = st.selectbox("Saving Accounts", ['little', 'moderate', 'rich', 'quite rich'])
checking_account = st.selectbox("Checking Account", ['little', 'moderate', 'rich'])
credit_amount = st.number_input("Credit amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

purpose = st.selectbox(
    "Purpose",
    ['car','furniture/equipment','radio/TV','education',
     'business','domestic appliances','repairs','vacation/others']
)

# Create DataFrame
input_df = pd.DataFrame({
    'Age':[age],
    'Sex':[encoders['Sex'].transform([sex])[0]],
    'Job':[job],
    'Housing':[encoders['Housing'].transform([housing])[0]],
    'Saving accounts':[encoders['Saving accounts'].transform([saving_accounts])[0]],
    'Checking account':[encoders['Checking account'].transform([checking_account])[0]],
    'Credit amount':[credit_amount],
    'Duration':[duration],
    'Purpose':[encoders['Purpose'].transform([purpose])[0]]
})

input_df = input_df[model.feature_names_in_]

# Prediction
if st.button("Predict Risk"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("The Predicted credit risk is: GOOD")
    else:
        st.error("The Predicted credit risk is: BAD")