#Task 2.7: Public Health 
# Import required libraries
import pandas as pd  # Data manipulation and analysis
import numpy as np   # Numerical operations
import matplotlib.pyplot as plt  # Basic plotting functionality
import seaborn as sns  # Enhanced visualization library
from scipy import stats  # Statistical functions

# Load dataset from GitHub repository
url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv"
df = pd.read_csv(url)  # Create DataFrame from CSV data

# -------------------
# INITIAL DATA EXPLORATION
# -------------------
print("First 5 rows of dataset:")
print(df.head())  # Display initial data structure

print("\nDataset metadata:")
print(df.info())  # Show column names, data types, and non-null counts

print("\nMissing values summary:")
print(df.isnull().sum())  # Count NaN values per column

# -------------------
# DATA CLEANING
# -------------------
df = df.fillna(0)  # Replace missing values with 0

# -------------------
# DISTRIBUTION ANALYSIS
# -------------------
variables = ['BMI', 'Weight', 'Age']  # Numerical variables to analyze

# Generate distribution plots for selected variables
for var in variables:
    plt.figure(figsize=(6, 4))  # Set plot dimensions
    sns.histplot(df[var], bins=30, kde=True, color='blue')  # Histogram with density curve
    plt.title(f'Distribution of {var}')  # Set plot title
    plt.show()  # Display plot

    # Weight conversion (Note: Should be outside loop to avoid redundant calculations)
    df['Weight_Pounds'] = df['Weight'] * 2.2  # Convert kg to pounds

# Display converted weight distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['Weight_Pounds'], bins=30, kde=True, color='green')
plt.title('Weight Distribution in Pounds')
plt.show()

# -------------------
# DESCRIPTIVE STATISTICS
# -------------------
print("\nKey Statistics:")
print("Average pulse rate:", df['Pulse'].mean())
print("Blood pressure range:", df['DiastolicBP'].min(), "-", df['DiastolicBP'].max())
print("Income variance:", df['Income'].var())
print("Income standard deviation:", df['Income'].std())

# -------------------
# RELATIONSHIP VISUALIZATION
# -------------------
categories = ['Gender', 'Diabetes', 'Smoking']  # Categorical variables for grouping

# Generate categorical scatter plots
for category in categories:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Height', y='Weight', hue=category, data=df)  # Color by category
    plt.title(f'Height vs Weight by {category}')
    plt.show()

# Combined comparison plot
plt.figure(figsize=(15, 5))  # Wider figure for side-by-side plots

# Gender comparison subplot
plt.subplot(1, 3, 1)  # Create first of three subplots
sns.scatterplot(x='Height', y='Weight', hue='Gender', data=df)
plt.title('Gender Comparison')

# Diabetes status subplot
plt.subplot(1, 3, 2)
sns.scatterplot(x='Height', y='Weight', hue='Diabetes', data=df)
plt.title('Diabetes Status')

# Smoking status subplot
plt.subplot(1, 3, 3)
sns.scatterplot(x='Height', y='Weight', hue='Smoking', data=df)
plt.title('Smoking Status')

plt.tight_layout()  # Improve spacing between subplots
plt.show()

# -------------------
# STATISTICAL HYPOTHESIS TESTING
# -------------------
# Compare age distributions between genders
male_age = df[df['Gender'] == 'Male']['Age']
female_age = df[df['Gender'] == 'Female']['Age']
t_stat, p_value = stats.ttest_ind(male_age, female_age, equal_var=False)
print("\nStatistical Tests Results:")
print(f"Age vs Gender T-test p-value: {p_value:.4f}")

# Compare BMI between diabetes groups
bmi_no_diabetes = df[df['Diabetes'] == 'No']['BMI']
bmi_yes_diabetes = df[df['Diabetes'] == 'Yes']['BMI']
t_stat, p_value = stats.ttest_ind(bmi_no_diabetes, bmi_yes_diabetes, equal_var=False)
print(f"BMI vs Diabetes T-test p-value: {p_value:.4f}")

# Compare alcohol consumption by relationship status
alcohol_single = df[df['Relationship'] == 'Single']['AlcoholYear']
alcohol_married = df[df['Relationship'] == 'Married']['AlcoholYear']
t_stat, p_value = stats.ttest_ind(alcohol_single, alcohol_married, equal_var=False)
print(f"Alcohol vs Relationship T-test p-value: {p_value:.4f}")
