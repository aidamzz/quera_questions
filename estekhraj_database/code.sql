-- Section1
SELECT id AS order_id FROM  orders 
ORDER BY order_id DESC;
-- Section2
SELECT id AS customer_id ,name AS customer_name FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
WHERE orders.id = NULL ORDER BY customer_name;
-- Section3
        
            

