import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("dataset/student.csv")

# Create line chart
plt.figure(figsize=(8,5))
plt.plot(data["math_score"], marker="o")

plt.title("Math Scores of Students")
plt.xlabel("Student Number")
plt.ylabel("Math Score")

plt.savefig("images/line_chart.png")
plt.show()