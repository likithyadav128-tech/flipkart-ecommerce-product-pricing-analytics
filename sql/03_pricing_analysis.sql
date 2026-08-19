USE flipkart_analysis;


-- ==========================================
-- 1. Average MRP vs Selling Price
-- ==========================================

SELECT
    ROUND(AVG(mrp), 2) AS average_mrp,
    ROUND(AVG(selling_price), 2) AS average_selling_price
FROM products;


-- ==========================================
-- 2. Highest Discount Products
-- ==========================================

SELECT
    title,
    mrp,
    selling_price,
    discount_amount,
    discount_percentage
FROM products
ORDER BY discount_percentage DESC
LIMIT 10;


-- ==========================================
-- 3. Lowest Discount Products
-- ==========================================

SELECT
    title,
    mrp,
    selling_price,
    discount_percentage
FROM products
ORDER BY discount_percentage ASC
LIMIT 10;


-- ==========================================
-- 4. Average Discount by Category
-- ==========================================

SELECT
    category_1,
    ROUND(AVG(discount_percentage), 2)
        AS average_discount
FROM products
GROUP BY category_1
ORDER BY average_discount DESC;


-- ==========================================
-- 5. Average Price by Category
-- ==========================================

SELECT
    category_1,
    ROUND(AVG(selling_price), 2)
        AS average_selling_price
FROM products
GROUP BY category_1
ORDER BY average_selling_price DESC;


-- ==========================================
-- 6. Products by Price Category
-- ==========================================

SELECT
    price_category,
    COUNT(*) AS product_count
FROM products
GROUP BY price_category
ORDER BY product_count DESC;


-- ==========================================
-- 7. Products by Discount Category
-- ==========================================

SELECT
    discount_category,
    COUNT(*) AS product_count
FROM products
GROUP BY discount_category
ORDER BY product_count DESC;