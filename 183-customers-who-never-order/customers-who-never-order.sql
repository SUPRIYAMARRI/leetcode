SELECT name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.CustomerId
WHERE CustomerId IS NULL;
