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


# ---  VISUALIZATION ---

# First plot
# Count values in the Ethnicity_Decoded column
ethnicity_counts = df['Ethnicity_Decoded'].value_counts()
print(ethnicity_counts)

# Bar plot of ethnicity counts
plt.figure(figsize=(8,5))
ethnicity_counts.plot(kind='bar', color='green')
plt.title("Number of Students per Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Second plot

# Data Preparation: Count the occurrences of 'Gender' for each 'Ethnicity_Decoded'
# We group by both columns and count the occurrences, then use unstack() 
# to pivot the 'Gender' counts into columns, suitable for grouped plotting.
count_data = df.groupby(['Ethnicity_Decoded', 'Gender']).size().unstack()

# Define the correct order of ethnicities for the X-axis, matching the first plot
order = ['Caucasian', 'African American', 'Asian', 'Other']
# Reindex the DataFrame to impose the correct order on the X-axis
count_data = count_data.reindex(order)

# define custom colors (skyblue for Male, pink for Female)
gender_labels_map = {0: 'Male', 1: 'Female'}
count_data = count_data.rename(columns=gender_labels_map)
custom_colors = ['darkturquoise', 'deeppink']

# Plotting using Matplotlib's plot.bar() method
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the grouped bar chart directly from the resulting DataFrame
count_data.plot(kind='bar', ax=ax, width=0.8, color=custom_colors)

# Customization and Visualization
ax.set_title('Number of Students on by Ethnicity and Gender', fontsize=16, pad=20)
ax.set_xlabel('Ethnicity', fontsize=12)
ax.set_ylabel('Counts', fontsize=12)

# Rotate X-axis labels for better readability
plt.xticks(rotation=45, ha='right') 

# Move the legend
ax.legend(title='Gender', loc='upper right')

# Add horizontal grid lines
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
