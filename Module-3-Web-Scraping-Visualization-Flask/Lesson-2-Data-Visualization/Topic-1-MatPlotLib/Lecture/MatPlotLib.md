# 📊 Introduction to Data Visualization with Matplotlib

## Part 1: Installation 🛠️

Matplotlib is: a comprehensive library for creating static, animated, and interactive visualizations in Python.

### Steps to Install Matplotlib:

Have Python and pip already installed. Then run:

```bash
pip install matplotlib
```

## Part 2: Matplotlib Basics 🎨

### Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

### Simple Plot Example

The basic components of a plot—figure, axis, line, labels. Simple example:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Simple Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.show()
```

### Plotting from a DataFrame

Matplotlib integrates well with Pandas, making it a handy tool for plotting data directly from DataFrames.

## Part 3: Visualizing Hockey Data 🏒

### Visualizing Win Percentage Over Time for the Calgary Flames

```python
import matplotlib.pyplot as plt

# Ensure team_trend is loaded with the Calgary Flames data as per the previous assignment
plt.figure(figsize=(10, 5))
plt.plot(team_trend['Year'], team_trend['Win Percentage'], marker='o')
plt.title("Calgary Flames - Win Percentage Over Years")
plt.xlabel("Year")
plt.ylabel("Win Percentage")
plt.grid(True)
plt.show()
```

### Comparing Team Performances in 2010

Explain how bar charts can be used to compare categorical data.

```python
# Ensure top_teams_2010 is loaded with the data as per the previous assignment
plt.figure(figsize=(12, 8))
plt.bar(top_teams_2010['Team Name'], top_teams_2010['Win Percentage'])
plt.title("Win Percentage of NHL Teams in 2010")
plt.xlabel("Team Name")
plt.xticks(rotation=45)  # Rotate team names for better visibility
plt.ylabel("Win Percentage")
plt.show()
```

### Advanced Visualization: Goal Differentials

Introduce scatter plots by comparing 'Goals For' versus 'Goals Against' for all teams, highlighting teams with the best and worst goal differentials.

```python
plt.figure(figsize=(10, 6))
plt.scatter(df_hockey['Goals For'], df_hockey['Goals Against'], c=df_hockey['Goal Differential'], cmap='coolwarm', s=100)
plt.colorbar(label='Goal Differential')  # Adds a color bar to indicate goal differential
plt.title("Goal For vs. Goal Against (Colored by Goal Differential)")
plt.xlabel("Goals For")
plt.ylabel("Goals Against")
plt.grid(True)
plt.show()
```

## Conclusion 🏁

### Q&A

Allocate time for questions and answers, encouraging students to discuss any difficulties or insights they encountered while working with Matplotlib and their hockey data.
