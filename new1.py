import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('modeltest.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict smoking status based on user input
def predict_smoking_status(user_input):
    # Preprocess user input
    input_df = pd.DataFrame(user_input, index=[0])
    
    # Predict smoking status
    prediction = model.predict(input_df)
    print("Prediction:", prediction)
    return prediction

# Create a Streamlit user interface
def main():
    st.title('Smoking Status Prediction')
    st.write('Enter the details below to predict smoking status:')
    
    # User input fields
    age = st.number_input('Age', min_value=0)
    height = st.number_input('Height (cm)', min_value=0)
    weight = st.number_input('Weight (kg)', min_value=0)
    waist = st.number_input('Waist (cm)', min_value=0.0)
    eyesight_left = st.number_input('Eyesight Left', min_value=0.0)
    eyesight_right = st.number_input('Eyesight Right', min_value=0.0)
    hearing_left = st.number_input('Hearing Left', min_value=0.0)
    hearing_right = st.number_input('Hearing Right', min_value=0.0)
    systolic = st.number_input('Systolic', min_value=0.0)
    relaxation = st.number_input('Relaxation', min_value=0.0)
    fasting_blood_sugar = st.number_input('Fasting Blood Sugar', min_value=0.0)
    cholesterol = st.number_input('Cholesterol', min_value=0.0)
    triglyceride = st.number_input('Triglyceride', min_value=0.0)
    hdl = st.number_input('HDL', min_value=0.0)
    ldl = st.number_input('LDL', min_value=0.0)
    hemoglobin = st.number_input('Hemoglobin', min_value=0.0)
    urine_protein = st.number_input('Urine Protein', min_value=0.0)
    serum_creatinine = st.number_input('Serum Creatinine', min_value=0.0)
    ast = st.number_input('AST', min_value=0.0)
    alt = st.number_input('ALT', min_value=0.0)
    gtp = st.number_input('GTP', min_value=0.0)
    dental_caries = st.number_input('Dental Caries', min_value=0.0)
    
    # Create a dictionary with user input
    user_input = {
        'age': age,
        'height': height,
        'weight': weight,
        'waist': waist,
        'eyesight_left': eyesight_left,
        'eyesight_right': eyesight_right,
        'hearing_left': hearing_left,
        'hearing_right': hearing_right,
        'systolic': systolic,
        'relaxation': relaxation,
        'fasting_blood_sugar': fasting_blood_sugar,
        'cholesterol': cholesterol,
        'triglyceride': triglyceride,
        'hdl': hdl,
        'ldl': ldl,
        'hemoglobin': hemoglobin,
        'urine_protein': urine_protein,
        'serum_creatinine': serum_creatinine,
        'ast': ast,
        'alt': alt,
        'gtp': gtp,
        'dental_caries': dental_caries,
    }
    
    # Predict smoking status when button is clicked
    if st.button('Predict'):
        smoking_status = predict_smoking_status(user_input)
        st.write(f'Predicted smoking status: {smoking_status}')

if __name__ == '__main__':
    main()
    