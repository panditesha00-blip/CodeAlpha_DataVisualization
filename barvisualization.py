import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("dataset/student.csv")

# Calculate average marks
subjects = ["Math", "Reading", "Writing"]
average_scores = [
    data["math_score"].mean(),
    data["reading_score"].mean(),
    data["writing_score"].mean()
]

# Create a bar chart
plt.bar(subjects, average_scores)

# Add title and labels
plt.title("Average Scores of Students")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

# Save the graph
plt.savefig("images/bar_chart.png")

# Display the graph
plt.show()