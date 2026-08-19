CREATE DATABASE IF NOT EXISTS flipkart_analysis;

USE flipkart_analysis;


CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    
    category_1 VARCHAR(255),
    category_2 VARCHAR(255),
    category_3 VARCHAR(255),
    
    title TEXT,
    
    product_rating DECIMAL(3,2),
    
    selling_price DECIMAL(12,2),
    mrp DECIMAL(12,2),
    
    seller_name VARCHAR(255),
    seller_rating DECIMAL(3,2),
    
    description TEXT,
    highlights TEXT,
    image_links TEXT,
    
    discount_amount DECIMAL(12,2),
    discount_percentage DECIMAL(6,2),
    
    price_category VARCHAR(50),
    discount_category VARCHAR(50)
);