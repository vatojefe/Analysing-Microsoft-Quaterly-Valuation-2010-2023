from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.api as sm

# Define the data
data = {
    'Years (Quarterly)': [2010, 2010.25, 2010.5, 2010.75, 2011, 2011.25, 2011.5, 2011.75,
                          2012, 2012.25, 2012.5, 2012.75, 2013, 2013.25, 2013.5, 2013.75,
                          2014, 2014.25, 2014.5, 2014.75, 2015, 2015.25, 2015.5, 2015.75,
                          2016, 2016.25, 2016.5, 2016.75, 2017, 2017.25, 2017.5, 2017.75,
                          2018, 2018.25, 2018.5, 2018.75, 2019, 2019.25, 2019.5, 2019.75,
                          2020, 2020.25, 2020.5, 2020.75, 2021, 2021.25, 2021.5, 2021.75,
                          2022, 2022.25, 2022.5, 2022.75, 2023, 2023.25, 2023.5, 2023.75],
    'Revenue (Billions Dollar)': [14.5, 16, 25, 19.95, 16.4, 17.3, 17.3, 20.8,
                                   17.4, 18.8, 16, 21.4, 20.4, 23.38, 23.2, 26.4,
                                   20.4, 23.38, 23.2, 26.4, 21.72, 22.18, 23.76, 20.53,
                                   26.4, 21.92, 25.82, 25.82, 23.21, 25.6, 24.53, 28.91,
                                   26.81, 30.08, 29.08, 32.47, 33.71, 33.05, 36.9, 36.9,
                                   35.02, 33.71, 33.05, 36.9, 35.02, 38.63, 38.63, 37.15,
                                   43.07, 41.7, 46.15, 45.31, 51.74, 52.85, 56.18, 56.51]
}

# Create DataFrame
df = pd.DataFrame(data)

# Perform linear regression for revenue
X = df['Years (Quarterly)']
X = sm.add_constant(X)  # Adding constant for intercept
y = df['Revenue (Billions Dollar)']
model = sm.OLS(y, X).fit()

# Print regression summary

predictions = model.predict(X)


# Plot regression line
plt.scatter(df['REVENUE$(IN BILLIONS OF DOLLARS)'], df['PROFIT$(IN BILLIONS OF DOLLARS)'], color='blue')
plt.plot(df['REVENUE$(IN BILLIONS OF DOLLARS)'], predictions, color='red')
plt.xlabel('Revenue (in billions of dollars)')
plt.ylabel('Profit (in billions of dollars)')
plt.title('Linear Regression: Revenue vs Profit')
plt.show()
