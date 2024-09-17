import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("bb_data.csv")

# Convert the Date column to datetime if it's not already
df["Date"] = pd.to_datetime(df["Date"])

# Calculate the average
average_gallons = df["Gallons"].mean()

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df["Date"], df["Gallons"])
plt.axhline(
    y=average_gallons,
    color="r",
    linestyle="--",
    label=f"Average ({average_gallons:.2f} gallons)",
)

# Customize the chart
plt.title("Gallons Pumped by Date")
plt.xlabel("Date")
plt.ylabel("Gallons Pumped")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as a PNG file
plt.savefig("gallons_pumped_chart.png")

print(
    f"Chart saved as gallons_pumped_chart.png with average line at {average_gallons:.2f} gallons"
)
