import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("dataset/student.csv")

# Create histogram
plt.figure(figsize=(8,5))
plt.hist(data["math_score"], bins=5)

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")

plt.show()