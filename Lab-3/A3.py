import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def create_target_variable(df, threshold=200):
    df['Class'] = np.where(df['Payment (Rs)'] > threshold, 'RICH', 'POOR')
    return df['Class']

def train_logistic_regression(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Load data
    file_path = 'Lab Session1 Data.xlsx'
    sheet_name = 'Purchase data'
    df = load_data(file_path, sheet_name)

    # Create features and target variable
    X = df.iloc[:, 1:4]
    y = create_target_variable(df)

    # Train logistic regression model
    model, X_train, X_test, y_train, y_test = train_logistic_regression(X, y)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    # Print results
    print("Model Accuracy:", accuracy)
