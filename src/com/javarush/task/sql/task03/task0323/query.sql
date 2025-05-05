-- Write your code here:
SELECT surname.last_name, orders.order_id from customers as surname left join orders on surname.customer_id = orders.customer_id