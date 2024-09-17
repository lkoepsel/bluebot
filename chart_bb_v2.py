import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("bb_data.csv")

# Convert the Date column to datetime if it's not already
df["Date"] = pd.to_datetime(df["Date"])

# Calculate the average
average_gallons = df["Gallons"].mean()

# Create a new column with date and day of week
df["Date_DayOfWeek"] = df["Date"].dt.strftime("%Y-%m-%d\n%a")

# Create the bar chart
plt.figure(figsize=(14, 6))  # Increased width to accommodate more text on x-axis
bars = plt.bar(df["Date_DayOfWeek"], df["Gallons"])

# Add a horizontal line at the average
plt.axhline(
    y=average_gallons,
    color="r",
    linestyle="--",
    label=f"Average ({average_gallons:.0f} gallons)",
)

# Customize the chart
plt.title("Gallons Pumped by Date")
plt.xlabel("Date")
plt.ylabel("Gallons Pumped")
plt.xticks(rotation=45, ha="right")
plt.legend()

# Adjust layout to prevent cutting off x-axis labels
plt.tight_layout()

# Save the chart as a PNG file
plt.savefig("gallons_pumped_chart.png")

print(
    f"Chart saved as gallons_pumped_chart.png with average line at {average_gallons:.2f} gallons"
)
