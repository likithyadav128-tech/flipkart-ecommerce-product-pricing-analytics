USE flipkart_analysis;


-- 1. Total number of products

SELECT
    COUNT(*) AS total_products
FROM products;


-- 2. Total sellers

SELECT
    COUNT(DISTINCT seller_name) AS total_sellers
FROM products;


-- 3. Total categories

SELECT
    COUNT(DISTINCT category_1) AS total_categories
FROM products;


-- 4. Average selling price

SELECT
    ROUND(AVG(selling_price), 2) AS average_selling_price
FROM products;


-- 5. Average product rating

SELECT
    ROUND(AVG(product_rating), 2) AS average_product_rating
FROM products;


-- 6. Average seller rating

SELECT
    ROUND(AVG(seller_rating), 2) AS average_seller_rating
FROM products;


-- 7. Average discount

SELECT
    ROUND(AVG(discount_percentage), 2) AS average_discount_percentage
FROM products;