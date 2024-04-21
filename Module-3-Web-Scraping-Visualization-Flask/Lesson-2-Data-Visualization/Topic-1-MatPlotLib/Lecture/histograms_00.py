import pandas as pd
import json
import matplotlib.pyplot as plt

# Load the JSON data into a Pandas DataFrame
json_data = """
[
    { "Student": "Alice", "Study": 35, "Sports": 5, "Leisure": 15, "Sleep": 60 },
    { "Student": "Bob", "Study": 20, "Sports": 10, "Leisure": 30, "Sleep": 60 },
    { "Student": "Chloe", "Study": 40, "Sports": 3, "Leisure": 10, "Sleep": 57 },
    { "Student": "David", "Study": 15, "Sports": 20, "Leisure": 40, "Sleep": 50 },
    { "Student": "Emma", "Study": 30, "Sports": 6, "Leisure": 20, "Sleep": 55 }
]
"""
data = json.loads(json_data)
df = pd.DataFrame(data)

# Task 1: Examine and describe data
print(df.head())  # Printing the first five rows

# Task 2: Create a basic histogram for 'Study' hours
plt.figure(figsize=(8, 6))
plt.hist(df["Study"], bins=5, color="blue", alpha=0.7)
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("study_hours_distribution.png")  # Save the figure
plt.close()  # Close the plot to free up memory

# Interpretation: Brief analysis
# The histogram shows that most students study between 15 to 40 hours, with a peak around 30-35 hours.


# Task 3: Customize your histogram
custom_bins = [10, 15, 25, 35, 45]
plt.figure(figsize=(8, 6))
plt.hist(df["Study"], bins=custom_bins, color="green", alpha=0.7)
plt.title("Customized Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("custom_study_hours_distribution.png")  # Save the figure
plt.close()  # Close the plot to free up memory

# Explanation for choices:
# Chosen bin sizes to closely observe the distribution around the common study hours (15, 25, 35).


# Task 4: Additional data visualization
# Visualizing 'Leisure' hours
plt.figure(figsize=(8, 6))
plt.hist(df["Leisure"], bins=5, color="red", alpha=0.7)
plt.title("Distribution of Leisure Hours")
plt.xlabel("Leisure Hours")
plt.ylabel("Number of Students")
plt.grid(True)
plt.savefig("leisure_hours_distribution.png")  # Save the figure
plt.close()  # Close the plot to free up memory

# Comparison:
# The distribution of 'Leisure' hours is more spread compared to 'Study' hours, with more variation in how students spend their leisure time.
