import click
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


@click.command()
@click.argument("csv_filename", type=click.Path(exists=True))
@click.option(
    "--output",
    "-o",
    default="gallons_pumped_chart.png",
    help="Output filename for the chart",
)
def create_chart(csv_filename, output):
    """Create a bar chart from CSV data showing gallons pumped by date."""
    # Read the CSV file
    df = pd.read_csv(csv_filename)

    # Convert timestamp to datetime and set as index
    df["Date"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df.set_index("Date")

    # Group by date and sum the values
    daily_data = df.groupby(df.index.date)["value"].sum().reset_index()
    daily_data.columns = ["Date", "Gallons"]

    # Convert Date back to datetime for proper sorting and formatting
    daily_data["Date"] = pd.to_datetime(daily_data["Date"])

    # Sort the data by date
    daily_data = daily_data.sort_values("Date")

    # Calculate the average
    average_gallons = daily_data["Gallons"].mean()

    # Create a new column with date and day of week
    daily_data["Date_DayOfWeek"] = daily_data["Date"].dt.strftime("%Y-%m-%d %a")

    # Create the bar chart
    plt.figure(figsize=(16, 8))  # Increased size for better visibility
    bars = plt.bar(daily_data["Date_DayOfWeek"], daily_data["Gallons"])

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.0f}",
            ha="center",
            va="bottom",
        )

    # Add a horizontal line at the average
    plt.axhline(
        y=average_gallons,
        color="r",
        linestyle="--",
        label=f"Average ({average_gallons:.0f} gallons)",
    )

    # Customize the chart
    plt.title("Gallons Pumped by Date", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Gallons Pumped", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(fontsize=10)

    # Add gridlines
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Adjust layout to prevent cutting off x-axis labels
    plt.tight_layout()

    # Save the chart as a PNG file
    plt.savefig(output, dpi=300)

    click.echo(
        f"Chart saved as {output} with average line at {average_gallons:.2f} gallons"
    )


if __name__ == "__main__":
    create_chart()
