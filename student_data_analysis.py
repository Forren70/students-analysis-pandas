import pandas as pd
import matplotlib.pyplot as plt

# Define the file name containing the raw numeric data
file_name_csv = "C:/Users/Admin/Documents/GitHub/students-analysis-pandas/Student_performance_data.csv"

# Load the CSV file into a Pandas DataFrame (DF)
df = pd.read_csv(file_name_csv)

print("--- DataFrame Loaded Successfully from CSV ---")
print(df.head(5))

# --- CONVERSION DICTIONARIES ---

# 1. Ethnicity (0-3)
ethnicity_conversion = {
    0: 'Caucasian',
    1: 'African American',
    2: 'Asian',
    3: 'Other'
}

# 2. ParentalEducation (0-4)
education_conversion = {
    0: 'None',
    1: 'High School',
    2: 'Some College',
    3: "Bachelor's",
    4: 'Higher'
}

# 3. Tutoring (0: No, 1: Yes)
tutoring_conversion = {
    0: 'No',
    1: 'Yes'
}

# 4. Gender (0: Male, 1: Female)
gender_conversion = {
    0: 'Male',
    1: 'Female'
}

# 5. GradeClass (0: A, 4: F)
grade_conversion = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'F'
}


# --- APPLY CONVERSIONS TO CREATE NEW DECODED COLUMNS ---

df['Ethnicity_Decoded'] = df['Ethnicity'].map(ethnicity_conversion)
df['Education_Decoded'] = df['ParentalEducation'].map(education_conversion)
df['Tutoring_Decoded'] = df['Tutoring'].map(tutoring_conversion)
df['Gender_Decoded'] = df['Gender'].map(gender_conversion)
df['GradeClass_Decoded'] = df['GradeClass'].map(grade_conversion)


# --- VERIFICATION ---

# Quick print to show the 5 new decoded columns
print("\n--- NEW DECODED COLUMNS ADDED ---")
print(df[['Gender_Decoded', 'Ethnicity_Decoded', 'Education_Decoded', 'Tutoring_Decoded', 'GradeClass_Decoded']].head(5))


# --- EXPORT DECODED DATA ---

# Define the output file path for the DataFrame with the 20 columns
output_path = "C:/Users/Admin/Documents/GitHub/students-analysis-pandas/Student_performance_decoded.csv"

# Save the DataFrame to a new CSV file. 
df.to_csv(output_path, index=False)

# Print confirmation message after exporting
print("\n--- Data Export Successful ---")
print("Decoded file saved to:", output_path)


