import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Print the dataframe
print(df)

# Plotting Sales Data for Products A, B, and C
plt.figure(figsize=(12, 6))

# Line Plot
plt.subplot(1, 3, 1)
plt.plot(df['Month'], df['Product_A_Sales'], label='Product A', marker='o')
plt.plot(df['Month'], df['Product_B_Sales'], label='Product B', marker='o')
plt.plot(df['Month'], df['Product_C_Sales'], label='Product C', marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Trend Over Months')
plt.xticks(rotation=45)
plt.legend()

# Bar Plot
plt.subplot(1, 3, 2)
df.set_index('Month').plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Comparison')
plt.xticks(rotation=45)

# Scatter Plot
plt.subplot(1, 3, 3)
plt.scatter(df['Product_A_Sales'], df['Product_B_Sales'], label='Product A vs B', color='r')
plt.scatter(df['Product_B_Sales'], df['Product_C_Sales'], label='Product B vs C', color='b')
plt.xlabel('Product A/B Sales')
plt.ylabel('Product B/C Sales')
plt.title('Product Sales Correlation')
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig('plot.png')
