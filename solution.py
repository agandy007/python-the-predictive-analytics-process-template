# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Function to display basic info about the DataFrame
def display_basic_info(df):
    # Print the shape of the DataFrame
    print("DataFrame shape:", df.shape)
    # Print the info of the DataFrame
    print("DataFrame info:")
    df.info()

# Function to display counts of unique values in categorical columns
def display_categorical_counts(df):
    # Define a list of categorical columns
    categorical_cols = ['gender', 'marital_status', 'subscription_type', 'churned']
    # Loop through each column and print the value counts
    for col in categorical_cols:
        print(f"\nValue counts for {col}:")
        print(df[col].value_counts())

# Function to identify target and feature variables
def identify_target_and_features(df):
    # Identify the target variable
    target = 'churned'
    # Create a list of feature variables excluding 'customer_id' and the target
    features = [col for col in df.columns if col not in ['customer_id', target]]
    print("Target variable:", target)
    print("Feature variables:", features)

# Function to calculate and print NumPy statistics
def calculate_numpy_statistics(df):
    # Convert 'monthly_charges' to a NumPy array
    monthly_charges = df['monthly_charges'].values
    # Calculate mean, max, min, and std
    print("Mean of monthly charges:", np.mean(monthly_charges))
    print("Max of monthly charges:", np.max(monthly_charges))
    print("Min of monthly charges:", np.min(monthly_charges))
    print("Standard deviation of monthly charges:", np.std(monthly_charges))

# Function to create visualizations using matplotlib
def create_visualizations(df):
    # Create a histogram of 'monthly_charges'
    # Create a bar chart of 'subscription_type' counts
    # Create a scatter plot of 'monthly_charges' vs 'num_support_calls'
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    
    # Histogram of monthly_charges
    axes[0].hist(df['monthly_charges'], bins=10, color='skyblue')
    axes[0].set_title('Distribution of Monthly Charges')
    axes[0].set_xlabel('Monthly Charges')
    axes[0].set_ylabel('Frequency')

    # Bar chart of subscription_type
    subscription_counts = df['subscription_type'].value_counts()
    axes[1].bar(subscription_counts.index, subscription_counts.values, color='lightgreen')
    axes[1].set_title('Subscription Type Counts')
    axes[1].set_xlabel('Subscription Type')
    axes[1].set_ylabel('Count')

    fig.tight_layout()
    plt.savefig('/dev/null', format='png')

    # Scatter plot of monthly_charges vs num_support_calls
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = {'Yes': 'red', 'No': 'blue'}
    ax.scatter(df['monthly_charges'], df['num_support_calls'], c=df['churned'].map(colors))
    ax.set_title('Monthly Charges vs. Number of Support Calls')
    ax.set_xlabel('Monthly Charges')
    ax.set_ylabel('Number of Support Calls')
    ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', label='Churned', markersize=10, markerfacecolor='red'),
                       plt.Line2D([0], [0], marker='o', color='w', label='Not Churned', markersize=10, markerfacecolor='blue')])
    plt.savefig('/dev/null', format='png')

# Main block with hardcoded data
if __name__ == '__main__':
    # Create a DataFrame with hardcoded values
    df = pd.DataFrame({
        'customer_id': list(range(101, 111)),
        'age': [25, 34, 45, 23, 35, 42, 51, 37, 29, 40],
        'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'marital_status': ['Single', 'Married', 'Single', 'Divorced', 'Married', 'Single', 'Married', 'Divorced', 'Single', 'Married'],
        'subscription_type': ['Basic', 'Standard', 'Premium', 'Basic', 'Standard', 'Premium', 'Basic', 'Standard', 'Premium', 'Basic'],
        'monthly_charges': [50.0, 70.5, 80.0, 60.0, 75.5, 90.0, 55.0, 65.5, 85.0, 95.5],
        'num_support_calls': [1, 2, 0, 3, 1, 0, 4, 2, 1, 3],
        'contract_length_months': [12, 24, 36, 12, 24, 36, 12, 24, 36, 12],
        'churned': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
    })

    # Print the DataFrame
    print(df)

    # Example function calls
    display_basic_info(df)
    display_categorical_counts(df)
    identify_target_and_features(df)
    calculate_numpy_statistics(df)
    create_visualizations(df)
