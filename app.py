# -*- coding: utf-8 -*-
"""Overview of Colaboratory Features

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/basic_features_overview.ipynb
"""
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump, load
import numpy as np

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')  # Replace with your actual CSV file path
    return df

# Train the Random Forest model
def train_model(df):
    # Encoding categorical variables
    df_encoded = pd.get_dummies(df, columns=['salary'], drop_first=True)

    # Define features and target
    X = df_encoded.drop(columns=["left"])
    y = df_encoded["left"]

    # Feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.20, random_state=0)

    # Initialize KFold
    kf = KFold(n_splits=5, shuffle=True, random_state=31)

    # Train the model with cross-validation
    model = RandomForestClassifier(n_estimators=150, random_state=45)
    model_score = cross_val_score(model, X_scaled, y, cv=kf)
    st.write(f"Model Score (Cross-Validation): {np.mean(model_score) * 100:0.2f}%")

    # Fit the model
    model.fit(X_train, y_train)
    score = model.score(X_train, y_train) * 100
    st.write(f"Model Score (Training): {score:0.2f}%")

    # Predictions and evaluation
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions) * 100
    st.write(f"Model Score (Testing): {accuracy:0.2f}%")

    st.text(classification_report(y_test, predictions))

    return model, scaler, X  # Return model, scaler, and X

# Save the model
def save_model(model):
    dump(model, 'random_forest_model.joblib')

# Load the model
def load_model():
    return load('random_forest_model.joblib')

# Main function
def main():
    st.title("Employee Stay or Leave Prediction")

    # Load data
    df = load_data()

    # Train model if not already trained
    if 'model' not in st.session_state:
        model, scaler, X = train_model(df)  # Get scaler and X as well
        save_model(model)
        st.session_state.model = model
        st.session_state.scaler = scaler  # Store scaler in session state
        st.session_state.X = X  # Store X in session state
    else:
        model = st.session_state.model
        scaler = st.session_state.scaler  # Retrieve scaler from session state
        X = st.session_state.X  # Retrieve X from session state

    # User input
    st.sidebar.header("Input Features")
    
    # Satisfaction Level Input
    satisfaction_level = st.sidebar.number_input("Satisfaction Level", min_value=0.09, max_value=1.0, value=0.38, step=0.01)
    
    # Last Evaluation Input
    last_evaluation = st.sidebar.number_input("Last Evaluation", min_value=0.36, max_value=1.0, value=0.53, step=0.01)
    
    # Number of Projects Input
    number_project = st.sidebar.selectbox("Number of Projects", range(2, 8))
    
    # Average Monthly Hours Input
    average_montly_hours = st.sidebar.number_input("Average Monthly Hours", min_value=96, max_value=310, value=157, step=1)
    
    # Time Spent in Company Input
    time_spend_company = st.sidebar.selectbox("Time Spent in Company (Years)", range(2, 11))
    
    # Salary Selection
    salary = st.sidebar.selectbox("Salary Level", ["low", "medium", "high"])

    if st.sidebar.button("Predict"):
        # Prepare input data for prediction
        input_data = [[satisfaction_level, last_evaluation, number_project, average_montly_hours, time_spend_company, salary]]
        input_data = pd.DataFrame(input_data, columns=['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'salary'])

        # Get dummies for the input (only for salary)
        input_data = pd.get_dummies(input_data, drop_first=True)

        # Ensure input_data has the same columns as your training data
        input_data = input_data.reindex(columns=X.columns, fill_value=0)  # Align with training data

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make predictions
        prediction = model.predict(input_data_scaled)
        probabilities = model.predict_proba(input_data_scaled)[0]

        # Determine expected outcome
        expected_outcome = "STAY" if prediction[0] == 0 else "LEAVE"
        probability_stay = probabilities[0] * 100
        probability_leave = probabilities[1] * 100

        # Display results
        st.write(f"Employee Expected To: {expected_outcome}")
        st.write(f"Probability To Stay: {probability_stay:.1f}%")
        st.write(f"Probability To Leave: {probability_leave:.1f}%")

if __name__ == "__main__":
    main()
