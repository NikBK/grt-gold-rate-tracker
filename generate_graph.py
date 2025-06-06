import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # For custom tick calculations

# Load data
df = pd.read_csv("gold_rates.csv", parse_dates=['Date'])

# Extract Day and Month-Year
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.strftime('%b %Y')  # e.g., Apr 2025

# Plot
plt.figure(figsize=(14, 12))

grouped = df.groupby('Month')
markers = ['o', 's', '^', 'D', '*', 'x', 'v']  # Enough for 7 months
colors = plt.cm.tab10.colors  # Default color palette

for i, (month, group) in enumerate(grouped):
    group = group.sort_values(by='Day').drop_duplicates(subset='Day')  # Avoid duplicate days
    plt.plot(
        group['Day'],
        group['GRT Rate (approx)'],
        marker=markers[i % len(markers)],
        color=colors[i % len(colors)],
        label=month,
        linewidth=2
    )

# Custom Y-axis ticks at 10-unit intervals
min_rate = df['GRT Rate (approx)'].min()
max_rate = df['GRT Rate (approx)'].max()
start = int(np.floor(min_rate / 10) * 10)
end = int(np.ceil(max_rate / 10) * 10)
plt.yticks(np.arange(start, end + 1, 10))

plt.title("GRT Daily Gold Rate Trend by Month")
plt.xlabel("Day of Month")
plt.ylabel("GRT Rate (₹/gram)")
plt.xticks(range(1, 32))
plt.grid(True)

# Move legend outside plot
plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout(rect=[0, 0, 0.8, 1])  # Leave space on right

# Save
plt.savefig("gold_trend.png", bbox_inches='tight')
