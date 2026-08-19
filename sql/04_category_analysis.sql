USE flipkart_analysis;


-- ==========================================
-- 1. Number of products in each category
-- ==========================================

SELECT
    category_1,
    COUNT(*) AS product_count
FROM products
GROUP BY category_1
ORDER BY product_count DESC;


-- ==========================================
-- 2. Category performance
-- ==========================================

SELECT
    category_1,

    COUNT(*) AS product_count,

    ROUND(
        AVG(selling_price),
        2
    ) AS average_price,

    ROUND(
        AVG(product_rating),
        2
    ) AS average_rating,

    ROUND(
        AVG(discount_percentage),
        2
    ) AS average_discount

FROM products

GROUP BY category_1

ORDER BY product_count DESC;


-- ==========================================
-- 3. Subcategory analysis
-- ==========================================

SELECT
    category_2,
    COUNT(*) AS product_count,
    ROUND(AVG(selling_price), 2)
        AS average_price,
    ROUND(AVG(product_rating), 2)
        AS average_rating
FROM products
GROUP BY category_2
ORDER BY product_count DESC
LIMIT 20;


-- ==========================================
-- 4. Category with highest rating
-- ==========================================

SELECT
    category_1,
    ROUND(AVG(product_rating), 2)
        AS average_rating
FROM products
GROUP BY category_1
ORDER BY average_rating DESC
LIMIT 10;


-- ==========================================
-- 5. Category with highest discount
-- ==========================================

SELECT
    category_1,
    ROUND(AVG(discount_percentage), 2)
        AS average_discount
FROM products
GROUP BY category_1
ORDER BY average_discount DESC
LIMIT 10;