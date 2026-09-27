import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Student dataset.csv")
print(df.head())
print(df.info())

print("Average GPA by Designation")
print(df.groupby("Designation")["GPA"].mean())

print("Overall Stats")
print("Mean GPA:", np.mean(df["GPA"]))
print("Std Dev GPA:", np.std(df["GPA"]))

print("Top 5 Students")
print(df.sort_values(by="GPA", ascending=False).head(5))
# Bar chart - Average GPA by Designation
df.groupby("Designation")["GPA"].mean().plot(kind="bar", color="skyblue")
plt.title("Average GPA by Designation")
plt.ylabel("GPA")
plt.xlabel("Designation")
plt.savefig("gpa_chart.png")
plt.show()