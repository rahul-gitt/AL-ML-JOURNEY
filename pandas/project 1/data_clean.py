import pandas as pd
import numpy as np

# Read Dataset
df = pd.read_csv(
    r"C:\Users\ASUS\OneDrive\Desktop\AL-ML-JOURNEY\pandas\project 1\indian_employee_messy_dataset.csv"
)

# -----------------------------
# Check Missing Values
# -----------------------------
print("Missing Values in Each Column:\n")
print(df.isnull().sum())

# -----------------------------
# Fill Missing Values
# -----------------------------

# Numerical Columns
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Median is better because Salary has outliers
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

df["Performance_Score"] = df["Performance_Score"].fillna(
    df["Performance_Score"].median()
)

df["Attendance_Percentage"] = df["Attendance_Percentage"].fillna(
    df["Attendance_Percentage"].mean()
)

df["Bonus"] = df["Bonus"].fillna(df["Bonus"].median())

# Categorical Column
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

# -----------------------------
# Replace Infinity Values
# -----------------------------
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Fix Invalid Values
# -----------------------------

# Attendance cannot be more than 100
df.loc[df["Attendance_Percentage"] > 100,
       "Attendance_Percentage"] = 100

# Performance Score cannot be more than 100
df.loc[df["Performance_Score"] > 100,
       "Performance_Score"] = 100

# Age cannot be below 18
df.loc[df["Age"] < 18, "Age"] = 18

# -----------------------------
# Handle Salary Outliers (IQR Method)
# -----------------------------

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

median_salary = df["Salary"].median()

df.loc[df["Salary"] < lower_limit, "Salary"] = median_salary
df.loc[df["Salary"] > upper_limit, "Salary"] = median_salary

# -----------------------------
# Final Check
# -----------------------------
print("\nRemaining Missing Values:\n")
print(df.isnull().sum())

print("\nDuplicate Rows :", df.duplicated().sum())

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("Cleaned_data.csv", index=False)

print("\nDataset Cleaned Successfully!")