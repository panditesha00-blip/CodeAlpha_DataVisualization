import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv("dataset/student.csv")

# Count males and females
gender_count = data["gender"].value_counts()

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Gender Distribution")
plt.show()