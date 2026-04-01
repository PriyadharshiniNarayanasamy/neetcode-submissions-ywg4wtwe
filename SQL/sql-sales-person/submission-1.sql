-- Write your query below
SELECT DISTINCT s.name FROM sales_person s
LEFT JOIN orders o
ON s.sales_id = o.sales_id 
WHERE s.sales_id NOT IN
(SELECT DISTINCT o.sales_id FROM orders o 
JOIN company c ON o.com_id = c.com_id
WHERE c.name  = 'CRIMSON');