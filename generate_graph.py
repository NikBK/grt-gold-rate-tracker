import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load CSV
df = pd.read_csv("gold_rates.csv", parse_dates=['Date'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Gold Rate (22KT)'], label='Market Rate (22KT)')
plt.plot(df['Date'], df['GRT Rate (approx)'], label='GRT Rate', linestyle='--')

plt.title("Gold Price Trend (22KT) - Daily")
plt.xlabel("Date")
plt.ylabel("INR per Gram")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

# Format x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Every 2 days

# Save chart
plt.savefig("gold_trend.png")
