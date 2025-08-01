
 Retrieve checkNumber, paymentDate, and amount from the payments table

SELECT checkNumber, paymentDate, amount
FROM payments;

Retrieve orderDate, requiredDate, and status for orders that are 'In Process', sorted by orderDate descending

SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

Display firstName, lastName, and email of employees with job title 'Sales Rep', ordered by employeeNumber descending

SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

Retrieve all columns and records from the offices table

SELECT *
FROM offices;

Fetch productName and quantityInStock from products, sorted by buyPrice ascending, limited to 5 records

SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
