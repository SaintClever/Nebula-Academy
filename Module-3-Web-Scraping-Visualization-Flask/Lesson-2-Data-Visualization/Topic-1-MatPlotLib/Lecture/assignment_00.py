import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("student_scores.csv")
print(df.head())

subjects = ["Math", "English", "Science", "History"]
scores = [df[subject].values for subject in subjects]

"""Generate Box Plots: Create a box plot for each subject to visualize the distribution of scores. Use the basic box plot code provided in the lecture."""
plt.figure(figsize=(4, 4))
plt.boxplot(scores, labels=subjects)
plt.title("Studen Performance in Different Subjects")
plt.xlabel("Scores")
plt.ylabel("Subjects")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

""" Which subject has the greatest variability in scores? """
# Calculate the standard deviation for each subject
std_dev = df[subjects].std()

# Plot the standard deviations
plt.figure(figsize=(4, 4))
std_dev.plot(kind="bar", color="skyblue")
plt.title("Variability in Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Standard Deviation")
plt.xticks(rotation=45)
plt.show()

# Find the subject with the greatest variability
greatest_variability = std_dev.idxmax()
print("Subject with the greatest variability in scores:", greatest_variability)


""" Which subject has the highest median score? """
# Calculate the median score for each subject
median_scores = df[subjects].median()

# Find the subject with the highest median score
subject_highest_median = median_scores.idxmax()
highest_median_score = median_scores.max()

print("Subject with the highest median score:", subject_highest_median)
print("Highest median score:", highest_median_score)


"""Customize the Box Plot: Improve the appearance of the box plots by adding colors to the boxes, whiskers, caps, and medians. Refer to the customization section of the lecture."""
# Plot box plots with customized appearance
plt.figure(figsize=(10, 6))
boxprops = dict(color="blue", linewidth=2)
whiskerprops = dict(color="red", linewidth=2)
capprops = dict(color="green", linewidth=2)
medianprops = dict(color="orange", linewidth=2)

df[subjects].boxplot(
    boxprops=boxprops,
    whiskerprops=whiskerprops,
    capprops=capprops,
    medianprops=medianprops,
)

plt.title("Variability in Scores by Subject")
plt.ylabel("Score")
plt.xlabel("Subject")
plt.xticks(rotation=45)
plt.show()
plt.savefig("customized_box_plot.png")
