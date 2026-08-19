USE flipkart_analysis;


-- ==========================================
-- 1. Top sellers by number of products
-- ==========================================

SELECT
    seller_name,
    COUNT(*) AS product_count
FROM products
GROUP BY seller_name
ORDER BY product_count DESC
LIMIT 10;


-- ==========================================
-- 2. Seller performance
-- ==========================================

SELECT
    seller_name,

    COUNT(*) AS product_count,

    ROUND(
        AVG(seller_rating),
        2
    ) AS average_seller_rating,

    ROUND(
        AVG(product_rating),
        2
    ) AS average_product_rating,

    ROUND(
        AVG(selling_price),
        2
    ) AS average_selling_price,

    ROUND(
        AVG(discount_percentage),
        2
    ) AS average_discount

FROM products

GROUP BY seller_name

ORDER BY product_count DESC
LIMIT 20;


-- ==========================================
-- 3. Highest-rated sellers
-- ==========================================

SELECT
    seller_name,
    COUNT(*) AS product_count,
    ROUND(AVG(seller_rating), 2)
        AS average_seller_rating
FROM products
GROUP BY seller_name
HAVING COUNT(*) >= 5
ORDER BY average_seller_rating DESC
LIMIT 10;


-- ==========================================
-- 4. Sellers giving highest discounts
-- ==========================================

SELECT
    seller_name,
    COUNT(*) AS product_count,
    ROUND(AVG(discount_percentage), 2)
        AS average_discount
FROM products
GROUP BY seller_name
HAVING COUNT(*) >= 5
ORDER BY average_discount DESC
LIMIT 10;


-- ==========================================
-- 5. Sellers with highest average price
-- ==========================================

SELECT
    seller_name,
    COUNT(*) AS product_count,
    ROUND(AVG(selling_price), 2)
        AS average_price
FROM products
GROUP BY seller_name
HAVING COUNT(*) >= 5
ORDER BY average_price DESC
LIMIT 10;