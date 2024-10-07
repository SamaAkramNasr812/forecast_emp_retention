Here's the updated README with the new Streamlit and GitHub project links:

```markdown
# Employee Attrition Prediction App

## Description
The Employee Attrition Prediction App is a machine learning project designed to predict whether employees will leave a company based on various features such as satisfaction level, last evaluation, and average monthly hours. By utilizing a Random Forest Classifier, this app provides valuable insights for HR departments to understand employee retention and make informed decisions. The application features an interactive Streamlit interface that allows users to input employee data and receive predictions.

## Installation Instructions
To run the Employee Attrition Prediction App locally or on Streamlit, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SamaAkramNasr812/forecast_emp_retention.git
   cd forecast_emp_retention
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then create a virtual environment and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   You can run the app locally using:
   ```bash
   streamlit run app.py
   ```

## Usage
To use the Employee Attrition Prediction App, navigate to the Streamlit link: [Employee Attrition Prediction App](https://forecastempretention-wruvraccbmx73qspz48sap.streamlit.app/).

### Input Features
Users can input the following features in the sidebar:
- **Satisfaction Level**: A number between 0.09 and 1.0.
- **Last Evaluation**: A number between 0.36 and 1.0.
- **Number of Projects**: Select from 2 to 7.
- **Average Monthly Hours**: A number between 96 and 310.
- **Time Spent in Company (Years)**: Select from 2 to 10.
- **Salary Level**: Choose between low, medium, and high.

### Expected Outputs
Upon clicking "Predict", the app will display:
- The expected outcome (STAY or LEAVE).
- The probability of staying.
- The probability of leaving.

### Example
1. Enter a Satisfaction Level of 0.7.
2. Enter a Last Evaluation of 0.8.
3. Select 5 for the Number of Projects.
4. Enter Average Monthly Hours as 160.
5. Select 3 for Time Spent in Company.
6. Choose "medium" for Salary Level.
7. Click "Predict" to see the results.

## Features
- Interactive visualizations of employee data and attrition factors.
- Real-time predictions based on user inputs.
- Comprehensive data preprocessing and model training pipeline.
- Insights into employee satisfaction and retention metrics.

## Technologies Used
- **Programming Language**: Python
- **Framework**: Streamlit
- **Libraries**: Pandas, NumPy, Scikit-learn, Joblib
- **Data Source**: Employee Attrition Dataset

## Demo
You can access the live demo of the app here: [Employee Attrition Prediction App Demo](https://forecastempretention-wruvraccbmx73qspz48sap.streamlit.app/).

## Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Special thanks to the contributors of the libraries used in this project.
- Inspiration from various machine learning resources and tutorials.

## Contact Information
For any inquiries or feedback, please reach out via GitHub: [SamaAkramNasr812](https://github.com/SamaAkramNasr812).

## Additional Notes
Feel free to explore the code and modify the app as per your requirements. Feedback and suggestions for improvement are always welcome!
```

### Notes:
- Make sure to update the `requirements.txt` file in your repository to include all necessary dependencies.
- Adjust any other specific details as needed.
