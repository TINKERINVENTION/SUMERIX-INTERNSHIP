#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style for plots
sns.set_theme(style="whitegrid")

# Define file path
file_name = "student-mat.csv"

# Safe check for file existence
if not os.path.exists(file_name):
    print(f"Error: '{file_name}' not found in the current directory.")
    print("Please make sure the dataset is uploaded to your workspace folder.")
    exit(1)

# Load the dataset using the proper semicolon separator
df = pd.read_csv(file_name, sep=';')

# --- 1. Explore & Clean Data ---
print("--- Dataset Shape ---")
print(f"Rows: {df.shape}, Columns: {df.shape[1]}\n")

print("--- Data Types ---")
print(df.dtypes, "\n")

print("--- Missing Values ---")
print(df.isnull().sum(), "\n")

# Using len() completely avoids any tuple subtraction errors
initial_rows = len(df)
df = df.drop_duplicates()
current_rows = len(df)

print(f"Removed {initial_rows - current_rows} duplicate rows.\n")

# --- 2. Statistical Analysis Results ---
print("--- Statistical Analysis Results ---")

# Q1: Average final grade (G3)
avg_g3 = df['G3'].mean()
print(f"1. Average Final Grade (G3): {avg_g3:.2f}")

# Q2: How many students scored above 15?
high_scorers = df[df['G3'] > 15].shape
print(f"2. Number of students scoring above 15: {high_scorers}")

# Q3: Is study time correlated with performance?
correlation = df['studytime'].corr(df['G3'])
print(f"3. Correlation between study time and final grade: {correlation:.4f}")

# Q4: Which gender performs better on average?
gender_perf = df.groupby('sex')['G3'].mean()
print("\n4. Average score by Gender:")
print(gender_perf)

# --- 3. Visualizations ---
print("\nGenerating and saving plots...")
plt.figure(figsize=(18, 5))

# 1. Histogram of Grades
plt.subplot(1, 3, 1)
sns.histplot(df['G3'], bins=10, color='skyblue', kde=True, edgecolor='black')
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Grade")
plt.ylabel("Frequency")

# 2. Scatterplot: Study Time vs Grades
plt.subplot(1, 3, 2)
sns.scatterplot(data=df, x='studytime', y='G3', alpha=0.6, color='purple')
plt.title("Study Time vs. Final Grade")
plt.xlabel("Weekly Study Time")
plt.ylabel("Final Grade (G3)")

# 3. Bar Chart: Male vs Female Average Score
plt.subplot(1, 3, 3)
sns.barplot(data=df, x='sex', y='G3', errorbar=None, palette='pastel')
plt.title("Average Score by Gender")
plt.xlabel("Gender (F: Female, M: Male)")
plt.ylabel("Average Final Grade")

plt.tight_layout()
# Save the plot directly to your workspace directory
plt.savefig('student_performance_plots.png')
print("Plots successfully saved as 'student_performance_plots.png'!")
