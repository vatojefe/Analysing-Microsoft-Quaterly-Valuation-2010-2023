INSERT INTO financial_data (year_quarter, revenue, profit)
VALUES
('2010 Q1', 14.50, 11.74),
('2010 Q2', 16.00, 12.86),
('2010 Q3', 25.00, 13.05),
('2010 Q4', 19.95, 15.10),
('2011 Q1', 16.40, 12.53),
('2011 Q2', 17.30, 13.65),
('2011 Q3', 17.30, 13.59),
('2011 Q4', 20.80, 15.24),
('2012 Q1', 17.40, 13.40),
('2012 Q2', 18.80, 13.80),
('2012 Q3', 16.00, 11.84),
('2012 Q4', 21.40, 15.76),
('2013 Q1', 20.40, 15.70),
('2013 Q2', 23.38, 14.10),
('2013 Q3', 23.20, 13.30),
('2013 Q4', 26.40, 16.10),
('2014 Q1', 20.40, 14.10),
('2014 Q2', 23.38, 15.70),
('2014 Q3', 23.20, 14.90),
('2014 Q4', 26.40, 16.30),
('2015 Q1', 21.72, 14.50),
('2015 Q2', 22.18, 14.70),
('2015 Q3', 20.37, 13.10),
('2015 Q4', 23.76, 13.90),
('2016 Q1', 20.53, 12.80),
('2016 Q2', 26.40, 18.40),
('2016 Q3', 21.92, 14.00),
('2016 Q4', 25.82, 15.92),
('2017 Q1', 23.21, 15.10),
('2017 Q2', 25.60, 17.10),
('2017 Q3', 24.53, 16.20),
('2017 Q4', 28.91, 17.85),
('2018 Q1', 26.81, 17.50),
('2018 Q2', 30.08, 20.30),
('2018 Q3', 29.08, 19.10),
('2018 Q4', 32.47, 20.00),
('2019 Q1', 30.57, 20.40),
('2019 Q2', 33.71, 23.30),
('2019 Q3', 33.05, 22.64),
('2019 Q4', 36.90, 24.50),
('2020 Q1', 35.02, 24.60),
('2020 Q2', 33.71, 25.60),
('2020 Q3', 33.05, 26.10),
('2020 Q4', 36.90, 28.88),
('2021 Q1', 35.02, 28.60),
('2021 Q2', 38.63, 32.10),
('2021 Q3', 37.15, 31.60),
('2021 Q4', 43.07, 34.70),
('2022 Q1', 41.70, 33.70),
('2022 Q2', 46.15, 35.40),
('2022 Q3', 45.31, 34.60),
('2022 Q4', 51.74, 35.20),
('2023 Q1', 52.85, 36.70),
('2023 Q2', 56.18, 39.30),
('2023 Q3', 56.51, 40.20);
-- Revenue
SELECT 
    AVG(revenue) AS mean_revenue,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY revenue) AS median_revenue,
    STDDEV_POP(revenue) AS std_dev_revenue,
    VARIANCE(revenue) AS variance_revenue
FROM financial_data;

-- Profit
SELECT 
    AVG(profit) AS mean_profit,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY profit) AS median_profit,
    STDDEV_POP(profit) AS std_dev_profit,
    VARIANCE(profit) AS variance_profit
FROM financial_data;
SELECT * FROM financial_data;
SELECT 
    SUBSTRING(year_quarter, 1, 4) AS year,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM financial_data
GROUP BY SUBSTRING(year_quarter, 1, 4)
ORDER BY year;
-- Highest Revenue Quarter
SELECT year_quarter, revenue
FROM financial_data
ORDER BY revenue DESC
LIMIT 1;

-- Lowest Revenue Quarter
SELECT year_quarter, revenue
FROM financial_data
ORDER BY revenue
LIMIT 1;

-- Highest Profit Quarter
SELECT year_quarter, profit
FROM financial_data
ORDER BY profit DESC
LIMIT 1;

-- Lowest Profit Quarter
SELECT year_quarter, profit
FROM financial_data
ORDER BY profit
LIMIT 1;
SELECT 
    year_quarter,
    revenue,
    profit,
    (revenue - LAG(revenue) OVER (ORDER BY year_quarter)) / LAG(revenue) OVER (ORDER BY year_quarter) * 100 AS revenue_change_percentage,
    (profit - LAG(profit) OVER (ORDER BY year_quarter)) / LAG(profit) OVER (ORDER BY year_quarter) * 100 AS profit_change_percentage
FROM financial_data;
SELECT CORR(revenue, profit) AS correlation_coefficient
FROM financial_data;
-- Simple Moving Average (SMA) for Revenue and Profit
SELECT 
    year_quarter,
    AVG(revenue) OVER (ORDER BY year_quarter ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS revenue_sma,
    AVG(profit) OVER (ORDER BY year_quarter ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS profit_sma
FROM financial_data;
SELECT 
    year_quarter,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM financial_data
GROUP BY year_quarter
HAVING SUM(revenue) > 15 AND SUM(profit) > 15;

