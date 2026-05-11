import matplotlib.pyplot as plt
import pandas as pd

file = input()

# TODO: Read in the CSV file as a dataframe
df = pd.read_csv(file)

# TODO: Print the average of flight delays and flight cancellations
print(f"Average delays: {df['Delayed'].mean():.2f}")
print(f"Average cancellations: {df['Cancelled'].mean():.2f}")

# TODO: Create a lineplot of flight delays vs months
plt.figure()
plt.plot(df['Month'], df['Delayed'], label='Delays')

# TODO: In the same figure, create a lineplot of flight cancellations vs months
plt.plot(df['Month'], df['Cancelled'], label='Cancellations')

# TODO: Add axis labels, title, and legend
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of flights", fontsize=10)
plt.title("Flight status at LAX", fontsize=14)
plt.legend()

# Save figure as output_fig.png
plt.savefig("output_fig.png")
plt.close()
