import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("gold_rates.csv", parse_dates=['Date'])

# Extract Day and Month-Year
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.strftime('%b %Y')  # e.g., Apr 2025

# Plot
plt.figure(figsize=(12, 7))

grouped = df.groupby('Month')

for month, group in grouped:
    # Sort by day for correct line plotting
    group_sorted = group.sort_values(by='Day')
    plt.plot(
        group_sorted['Day'],
        group_sorted['GRT Rate (approx)'],
        marker='o',
        label=month
    )

plt.title("📈 GRT Daily Gold Rate Trend by Month")
plt.xlabel("Day of Month")
plt.ylabel("GRT Rate (₹/gram)")
plt.xticks(range(1, 32))
plt.grid(True)
plt.legend(title="Month", loc="upper left")
plt.tight_layout()

plt.savefig("gold_trend.png")
