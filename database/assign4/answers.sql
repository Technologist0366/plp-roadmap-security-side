Question 1: Total payment amount per date (Top 5 latest)

SELECT 
    paymentDate, 
    SUM(amount) AS total_amount
FROM 
    payments
GROUP BY 
    paymentDate
ORDER BY 
    paymentDate DESC
LIMIT 5;

Question 2: Average credit limit per customer (grouped by name and country)

SELECT 
    customerName, 
    country, 
    AVG(creditLimit) AS average_credit_limit
FROM 
    customers
GROUP BY 
    customerName, country;

Question 3: Total price per product ordered

SELECT 
    productCode, 
    quantityOrdered, 
    (quantityOrdered * priceEach) AS total_price
FROM 
    orderdetails
GROUP BY 
    productCode, quantityOrdered, priceEach;

Question 4: Highest payment amount per check number

SELECT 
    checkNumber, 
    MAX(amount) AS highest_amount
FROM 
    payments
GROUP BY 
    checkNumber;
