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
    'Profit (Billions Dollar)': [11.74, 12.86, 13.05, 15.1, 12.53, 13.65, 13.59, 15.24,
                                  13.4, 11.84, 15.75, 15.7, 14.1, 15.7, 13.3, 16.1,
                                  14.1, 15.7, 14.9, 16.3, 14.5, 14.7, 13.9, 12.8,
                                  18.4, 14, 15.92, 15.92, 15.1, 17.1, 16.2, 17.85,
                                  17.5, 20.3, 19.1, 23.3, 23.3, 22.64, 24.5, 24.6,
                                  25.6, 26.1, 26.1, 28.88, 28.6, 32.1, 32.1, 31.6,
                                  34.7, 33.7, 35.4, 34.6, 35.2, 36.7, 39.3, 40.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Perform linear regression
X = df['Years (Quarterly)']
X = sm.add_constant(X)  # Adding constant for intercept
y = df['Profit (Billions Dollar)']
model = sm.OLS(y, X).fit()

# Print regression summary
print(model.summary())


# Plot regression line
predictions = model.predict(X)

plt.scatter(df['YEAR'], df['PROFIT$(IN BILLIONS OF DOLLARS)'], color='blue')
plt.plot(df['YEAR'], predictions, color='red')
plt.xlabel('Year')
plt.ylabel('Profit (in billions of dollars)')
plt.title('Linear Regression: Year vs Profit')
plt.show()
