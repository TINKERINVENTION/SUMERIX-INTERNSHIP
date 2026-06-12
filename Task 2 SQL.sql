-- ====================================================================
-- Sumerix Global Internship: Task 2 SQL Analysis Script
-- Objectives: Schema Definition, Relational Joins, & KPI Computation
-- ====================================================================

-- 1. Create Schema Structure
CREATE TABLE IF NOT EXISTS Customers (
    Customer_ID VARCHAR(50) PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Region VARCHAR(50),
    Segment VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Orders (
    Order_ID VARCHAR(50) PRIMARY KEY,
    Order_Date DATE,
    Customer_ID VARCHAR(50),
    Product_Category VARCHAR(50),
    Sales DECIMAL(10,2),
    Quantity INT,
    Profit DECIMAL(10,2),
    Discount DECIMAL(4,2),
    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID)
);

-- 2. Validate Relational Inner Join 
SELECT 
    o.Order_ID,
    o.Order_Date,
    c.Customer_Name,
    c.Region,
    o.Product_Category,
    o.Sales,
    o.Profit
FROM Orders o
INNER JOIN Customers c ON o.Customer_ID = c.Customer_ID;

-- 3. Metric Calculations (Business KPIs)

-- KPI 1: Total Revenue Generation by Regional Boundaries
SELECT 
    c.Region,
    ROUND(SUM(o.Sales), 2) AS Total_Sales
FROM Orders o
JOIN Customers c ON o.Customer_ID = c.Customer_ID
GROUP BY c.Region
ORDER BY Total_Sales DESC;

-- KPI 2: Profit Margin Efficiency Tracking by Category
SELECT 
    Product_Category,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit) / SUM(Sales), 4) AS Profit_Margin
FROM Orders
GROUP BY Product_Category
ORDER BY Profit_Margin DESC;

-- KPI 3: Monthly Operational Sales Trend 
SELECT 
    EXTRACT(MONTH FROM Order_Date) AS Month_Number,
    ROUND(SUM(Sales), 2) AS Monthly_Revenue,
    COUNT(Order_ID) AS Total_Orders
FROM Orders
GROUP BY Month_Number
ORDER BY Month_Number ASC;

-- KPI 4: High-Value Customer Identification (Top 5 by Gross Revenue)
SELECT 
    c.Customer_Name,
    c.Segment,
    ROUND(SUM(o.Sales), 2) AS Total_Revenue
FROM Orders o
JOIN Customers c ON o.Customer_ID = c.Customer_ID
GROUP BY c.Customer_Name, c.Segment
ORDER BY Total_Revenue DESC
LIMIT 5;