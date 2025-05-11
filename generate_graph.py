import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load CSV
df = pd.read_csv("gold_rates.csv", parse_dates=['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.strftime('%b %Y')  # e.g. "May 2025"

# Group by month and plot each as a separate line
plt.figure(figsize=(12, 7))

for month, group in df.groupby('Month'):
    plt.plot(group['Day'], group['GRT Rate (approx)'], label=month)

plt.title("📈 GRT Daily Gold Rate Trend - Monthly Comparison")
plt.xlabel("Day of Month")
plt.ylabel("GRT Rate (₹/gram)")
plt.xticks(range(1, 32))
plt.legend(title="Month", loc="upper left")
plt.grid(True)
plt.tight_layout()

# Save graph
plt.savefig("gold_trend.png")
