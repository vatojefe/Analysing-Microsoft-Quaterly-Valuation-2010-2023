import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define your data
data = {
    'YEARS': ['2010 Q1', '2010 Q2', '2010 Q3', '2010 Q4', '2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4',
              '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4',
              '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4',
              '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4', '2017 Q1', '2017 Q2', '2017 Q3', '2017 Q4',
              '2018 Q1', '2018 Q2', '2018 Q3', '2018 Q4', '2019 Q1', '2019 Q2', '2019 Q3', '2019 Q4',
              '2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4', '2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4',
              '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3'],
    'REVENUE$(IN BILLIONS OF DOLLARS)': [14.50, 16.00, 25.00, 19.95, 16.40, 17.30, 17.30, 20.80,
                                          17.40, 18.80, 16.00, 21.40, 20.40, 23.38, 23.20, 26.40,
                                          20.40, 23.38, 23.20, 26.40, 21.72, 22.18, 20.37, 23.76,
                                          20.53, 26.40, 21.92, 25.82, 23.21, 25.60, 24.53, 28.91,
                                          26.81, 30.08, 29.08, 32.47, 30.57, 33.71, 33.05, 36.90,
                                          35.02, 33.71, 33.05, 36.90, 35.02, 38.63, 37.15, 43.07,
                                          41.70, 46.15, 45.31, 51.74, 52.85, 56.18, 56.51],
    'PROFIT$(IN BILLIONS OF DOLLARS)': [11.74, 12.86, 13.05, 15.10, 12.53, 13.65, 13.59, 15.24,
                                         13.40, 13.80, 11.84, 15.76, 15.70, 14.10, 13.30, 16.10,
                                         14.10, 15.70, 14.90, 16.30, 14.50, 14.70, 13.10, 13.90,
                                         12.80, 18.40, 14.00, 15.92, 15.10, 17.10, 16.20, 17.85,
                                         17.50, 20.30, 19.10, 20.00, 20.40, 23.30, 22.64, 24.50,
                                         24.60, 25.60, 26.10, 28.88, 28.60, 32.10, 31.60, 34.70,
                                         33.70, 35.40, 34.60, 35.20, 36.70, 39.30, 40.20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Remove dollar sign and convert to float
df['REVENUE$(IN BILLIONS OF DOLLARS)'] = df['REVENUE$(IN BILLIONS OF DOLLARS)'].astype(str).str.replace('[\$,]', '').astype(float)
df['PROFIT$(IN BILLIONS OF DOLLARS)'] = df['PROFIT$(IN BILLIONS OF DOLLARS)'].astype(str).str.replace('[\$,]', '').astype(float)

# Calculate mean and median for Revenue and Profit
revenue_mean = df['REVENUE$(IN BILLIONS OF DOLLARS)'].mean()
revenue_std = df['REVENUE$(IN BILLIONS OF DOLLARS)'].std()
revenue_median = df['REVENUE$(IN BILLIONS OF DOLLARS)'].median()

profit_mean = df['PROFIT$(IN BILLIONS OF DOLLARS)'].mean()
profit_std = df['PROFIT$(IN BILLIONS OF DOLLARS)'].std()
profit_median = df['PROFIT$(IN BILLIONS OF DOLLARS)'].median()

# Print mean, standard deviation, and median
print("Revenue Mean:", revenue_mean)
print("Revenue Standard Deviation:", revenue_std)
print("Revenue Median:", revenue_median)

print("Profit Mean:", profit_mean)
print("Profit Standard Deviation:", profit_std)
print("Profit Median:", profit_median)

# Create subplots
fig, axes = plt.subplots(2, 4, figsize=(15, 10))

# Histogram for Revenue
sns.histplot(df['REVENUE$(IN BILLIONS OF DOLLARS)'], bins=10, kde=True, color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('Revenue Distribution')
axes[0, 0].set_xlabel('Revenue (in billions of dollars)')
axes[0, 0].set_ylabel('Frequency')

# Bar chart for Profit
sns.barplot(data=df, x='YEARS', y='PROFIT$(IN BILLIONS OF DOLLARS)', palette='coolwarm', ax=axes[0, 1])
axes[0, 1].set_title('Profit Over Years')
axes[0, 1].set_xlabel('Years')
axes[0, 1].set_ylabel('Profit (in billions of dollars)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Scatter plot for Revenue and Profit
sns.scatterplot(data=df, x='REVENUE$(IN BILLIONS OF DOLLARS)', y='PROFIT$(IN BILLIONS OF DOLLARS)', color='green', ax=axes[0, 2])
axes[0, 2].set_title('Revenue vs Profit')
axes[0, 2].set_xlabel('Revenue (in billions of dollars)')
axes[0, 2].set_ylabel('Profit (in billions of dollars)')

# Line chart for Profit
df.plot(x='YEARS', y='PROFIT$(IN BILLIONS OF DOLLARS)', ax=axes[1, 0], color='orange')
axes[1, 0].set_title('Profit Over Years')
axes[1, 0].set_xlabel('Years')
axes[1, 0].set_ylabel('Profit (in billions of dollars)')
axes[1, 0].tick_params(axis='x', rotation=45)

# Box plot for Revenue
sns.boxplot(data=df, y='REVENUE$(IN BILLIONS OF DOLLARS)', ax=axes[1, 1])
axes[1, 1].set_title('Revenue Distribution')
axes[1, 1].set_ylabel('Revenue (in billions of dollars)')

# Box plot for Profit
sns.boxplot(data=df, y='PROFIT$(IN BILLIONS OF DOLLARS)', ax=axes[1, 2])
axes[1, 2].set_title('Profit Distribution')
axes[1, 2].set_ylabel('Profit (in billions of dollars)')
# Remove empty subplot
fig.delaxes(axes[1, 1])

# Remove empty subplot
fig.delaxes(axes[1, 2])

plt.tight_layout()
plt.show()

