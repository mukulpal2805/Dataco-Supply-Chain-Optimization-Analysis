-- Warehouse Performance Analysis
SELECT 
    warehouse,
    COUNT(DISTINCT order_id) as total_orders,
    SUM(order_item_quantity) as total_items,
    SUM(sales) as total_sales,
    AVG(delivery_time) as avg_delivery_time,
    SUM(CASE 
        WHEN delivery_time > 3 THEN 1 
        ELSE 0 
    END) as delayed_deliveries
FROM 
    supply_chain_data
GROUP BY 
    warehouse
ORDER BY 
    total_sales DESC;

-- Stock Analysis by Product Category
SELECT 
    product_category,
    SUM(order_item_quantity) as total_quantity,
    SUM(sales) as total_sales,
    COUNT(DISTINCT order_id) as number_of_orders,
    SUM(sales)/COUNT(DISTINCT order_id) as avg_order_value
FROM 
    supply_chain_data
GROUP BY 
    product_category
ORDER BY 
    total_sales DESC;
