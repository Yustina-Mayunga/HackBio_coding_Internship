# Import required libraries
import pandas as pd  # Data manipulation
import numpy as np  # Numerical operations
import matplotlib.pyplot as plt  # Plotting
import seaborn as sns  # Advanced visualization
from scipy import stats  # Statistical analysis

# -------------------
# DATA LOADING
# -------------------
url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/nhanes.csv"
df = pd.read_csv(url)  # Load dataset

# -------------------
# INITIAL DATA EXPLORATION
# -------------------
print("First 5 rows of dataset:")
print(df.head())  # Show first 5 rows

print("\nDataset metadata:")
df.info()  # Show column names, data types, and missing values

print("\nMissing values summary:")
print(df.isnull().sum())  # Count missing values in each column

# -------------------
# DATA CLEANING
# -------------------
df = df.fillna(0)  # Replace all missing values with 0

# -------------------
# DISTRIBUTION ANALYSIS (Histograms)
# -------------------
variables = ['BMI', 'Weight', 'Age']  # Columns to visualize

for var in variables:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[var], bins=30, kde=True, color='blue')
    plt.title(f'Distribution of {var}')
    plt.show()

# Convert weight from kg to pounds
df['Weight_Pounds'] = df['Weight'] * 2.2

# Histogram for Weight in Pounds
plt.figure(figsize=(6, 4))
sns.histplot(df['Weight_Pounds'], bins=30, kde=True, color='green')
plt.title('Weight Distribution in Pounds')
plt.show()

# -------------------
# DESCRIPTIVE STATISTICS
# -------------------
print("\nKey Statistics:")
print("Average pulse rate:", df['Pulse'].mean())
print("Blood pressure range:", df['BPDia'].min(), "-", df['BPDia'].max())
print("Income variance:", df['Income'].var())
print("Income standard deviation:", df['Income'].std())

# -------------------
# RELATIONSHIP VISUALIZATION (Scatter Plots)
# -------------------
# Ensure categorical variables are in string format
df['Gender'] = df['Gender'].astype(str)
df['Diabetes'] = df['Diabetes'].astype(str)
df['SmokingStatus'] = df['SmokingStatus'].astype(str)

# Scatter plots for height vs weight, colored by category
categories = ['Gender', 'Diabetes', 'SmokingStatus']

for category in categories:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x='Height', y='Weight', hue=category, data=df)
    plt.title(f'Height vs Weight by {category}')
    plt.show()

# Combined scatter plots
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.scatterplot(x='Height', y='Weight', hue='Gender', data=df)
plt.title('Height vs Weight by Gender')

plt.subplot(1, 3, 2)
sns.scatterplot(x='Height', y='Weight', hue='Diabetes', data=df)
plt.title('Height vs Weight by Diabetes Status')

plt.subplot(1, 3, 3)
sns.scatterplot(x='Height', y='Weight', hue='SmokingStatus', data=df)
plt.title('Height vs Weight by Smoking Status')

plt.tight_layout()
plt.show()

# -------------------
# STATISTICAL TESTS (T-Tests)
# -------------------
print("\nStatistical Tests Results:")

# T-Test: Age vs Gender
male_age = df[df['Gender'] == 'Male']['Age']
female_age = df[df['Gender'] == 'Female']['Age']
if male_age.var() > 0 and female_age.var() > 0:
    t_stat, p_value = stats.ttest_ind(male_age, female_age, equal_var=False)
    print(f"Age vs Gender T-test p-value: {p_value:.2f}")
else:
    print("Age vs Gender: One group has zero variance, t-test not possible.")

# T-Test: BMI vs Diabetes
bmi_no_diabetes = df[df['Diabetes'] == 'No']['BMI']
bmi_yes_diabetes = df[df['Diabetes'] == 'Yes']['BMI']
if bmi_no_diabetes.var() > 0 and bmi_yes_diabetes.var() > 0:
    t_stat, p_value = stats.ttest_ind(bmi_no_diabetes, bmi_yes_diabetes, equal_var=False)
    print(f"BMI vs Diabetes T-test p-value: {p_value:.2f}")
else:
    print("BMI vs Diabetes: One group has zero variance, t-test not possible.")

# T-Test: Alcohol Consumption vs Relationship Status
alcohol_single = df[df['RelationshipStatus'] == 'Single']['AlcoholYear']
alcohol_married = df[df['RelationshipStatus'] == 'Married']['AlcoholYear']
