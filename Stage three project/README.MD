Breast Cancer Classification and Clustering
Overview
This project explores a dataset of breast cancer tumor features to analyze and classify malignant (M) and benign (B) tumors. Using Principal Component Analysis (PCA) and K-Means Clustering, we attempt to reduce dimensionality and identify patterns in the dataset.

Dataset
The dataset is sourced from: Wisconsin Breast Cancer Dataset

Features:
Various numerical features related to tumor characteristics (e.g., radius, texture, smoothness, concave points, etc.).
The diagnosis column is the target variable (1 = Malignant, 0 = Benign).
Steps in the Analysis
1. Data Preprocessing
Load the dataset using pandas.
Drop the id column (not useful for analysis).
Convert diagnosis to numerical values (M → 1, B → 0).
Handle missing values by filling them with the column mean.
Standardize the numerical features using StandardScaler.
2. Dimensionality Reduction with PCA
Reduce the dataset to 5 principal components using PCA.
Analyze the explained variance ratio to determine how much variance is retained.
3. K-Means Clustering
Use the Elbow Method to determine the optimal number of clusters.
Apply K-Means clustering with K=2 (to match the number of diagnoses).
Compare the clusters with actual cancer diagnoses using a confusion matrix.
Calculate the clustering accuracy.
4. Visualization
Visualize PCA-transformed data in 2D scatter plots.
Plot clustering results for different values of K (from 2 to 5).
Results
The clustering approach groups the tumor samples into distinct clusters.
The accuracy score helps evaluate how well the clustering matches the true labels.
Visualizations provide insights into the data distribution.
Key Learnings
PCA helps in reducing dimensionality while preserving important information.
K-Means can cluster tumors effectively, though it may not be perfect.
Unsupervised learning techniques like clustering can help in discovering patterns in medical datasets.
Drug Discovery
Overview
This project focuses on predicting drug docking scores using machine learning techniques. Two regression models, Linear Regression and Random Forest Regression, are used to estimate docking scores based on chemical structure features.

Dataset
The dataset is obtained from: HackBio Internship Dataset

Data Preprocessing
The dataset is loaded using pandas.
Column names are converted to lowercase for consistency.
Only numeric columns are used for model training, excluding non-numeric fields like id and smiles.
The dataset is split into 80% training and 20% testing sets.
Models Used
Linear Regression: A simple regression model to establish baseline performance.
Random Forest Regression: An ensemble-based model for improved prediction accuracy.
Implementation Steps
1. Load and Preprocess Data
Load the dataset.
Extract numerical features.
Define the target variable (score).
Split data into training and testing sets.
2. Train Regression Models
Train a Linear Regression model and evaluate its Mean Squared Error (MSE).
Train a Random Forest Regressor with 100 estimators.
Compare the MSE values for both models.
3. Feature Importance Analysis
Extract feature importance scores from the Random Forest model.
Visualize the top contributing features using Seaborn bar plots.
4. Visualizing Model Predictions
Scatter plot comparing actual vs. predicted docking scores.
A reference diagonal line (y = x) is plotted for comparison.
Results
Mean Squared Error (MSE) values are computed for both models.
Feature importance analysis provides insight into the key chemical properties influencing docking scores.
Execution
Run the Python script to train the models and generate plots

Visualization Outputs
Feature Importance Plot: Highlights key features impacting docking scores.
Predicted vs Actual Scores Plot: Evaluates the model's predictive performance.
Conclusion
This project demonstrates the application of machine learning models for predicting drug docking scores, comparing Linear Regression and Random Forest Regression in terms of performance and interpretability.

Future Improvements
Hyperparameter tuning for Random Forest to optimize performance.
Feature engineering to enhance model accuracy.
Exploring deep learning models for improved predictions.
