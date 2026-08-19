# Flipkart E-Commerce Product & Pricing Analytics

## 📌 Project Overview

This project is an end-to-end **Flipkart E-Commerce Product & Pricing Analytics** project built using **Python, SQL, and Power BI**.

The goal is to analyze Flipkart product data and identify useful business insights related to:

- Product categories
- Subcategories
- Product pricing
- MRP and selling price
- Discounts
- Product ratings
- Seller ratings
- Seller performance
- Price categories
- Discount categories

> **Important:** The dataset is a product-level dataset and does not contain actual transaction quantity or revenue data. Therefore, this project focuses on product, pricing, category, rating, and seller analytics rather than sales/revenue forecasting.

---

## 🎯 Business Objectives

The project answers questions such as:

1. How many products are available?
2. Which categories contain the most products?
3. Which categories have the highest average ratings?
4. Which products have the highest discounts?
5. What is the average selling price?
6. Which sellers list the most products?
7. Which sellers have the highest ratings?
8. Which categories have the highest average discounts?
9. How are products distributed across price ranges?
10. Which products provide good value based on rating and discount?

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning and exploratory analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| MySQL | SQL analysis and business queries |
| Power BI | Interactive dashboard |
| DAX | KPI calculations |
| GitHub | Project version control |

---

## 📂 Project Structure

```text
flipkart-ecommerce-product-pricing-analytics/
│
├── data/
│   └── flipkart_products.csv
│
├── python/
│   ├── 01_load_and_clean.py
│   ├── 02_eda.py
│   ├── 03_pricing_analysis.py
│   ├── 04_brand_category_analysis.py
│   ├── 05_seller_analysis.py
│   └── 06_export_powerbi.py
│
├── sql/
│   ├── 01_create_table.sql
│   ├── 02_basic_analysis.sql
│   ├── 03_pricing_analysis.sql
│   ├── 04_category_analysis.sql
│   ├── 05_seller_analysis.sql
│   └── 06_business_insights.sql
│
├── output/
│   ├── cleaned_flipkart_products.csv
│   ├── pricing_analysis.csv
│   ├── category_1_analysis.csv
│   ├── category_2_analysis.csv
│   ├── category_3_analysis.csv
│   ├── seller_analysis.csv
│   └── PowerBI_Flipkart_Products.csv
│
├── powerbi/
│   └── Flipkart_Ecommerce_Analytics.pbix
│
├── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The project uses a publicly available Flipkart product dataset.

The dataset contains product-level information such as:

- Category 1
- Category 2
- Category 3
- Product title
- Product rating
- Selling price
- MRP
- Seller name
- Seller rating
- Description
- Highlights
- Image links

Additional analytical columns are created during the Python data-cleaning process:

- Discount amount
- Discount percentage
- Price category
- Discount category

---

# 🐍 Python Analysis

The Python workflow is divided into multiple files.

### 01_load_and_clean.py

Performs:

- Dataset loading
- Column cleaning
- Duplicate removal
- Data type conversion
- Price cleaning
- Rating cleaning
- Discount calculation
- Price category creation
- Clean dataset export

### 02_eda.py

Performs exploratory data analysis:

- Dataset information
- Missing-value analysis
- Product count
- Seller count
- Category count
- Price statistics
- Rating statistics
- Discount statistics
- Top categories
- Top brands where available
- Price distribution
- Rating distribution

### 03_pricing_analysis.py

Analyzes:

- MRP
- Selling price
- Discount amount
- Discount percentage
- Highest-discount products
- Discount categories
- Price comparison

### 04_brand_category_analysis.py

Analyzes:

- Main categories
- Subcategories
- Product counts
- Average price
- Average rating
- Average discount
- Category-level comparisons

> The downloaded dataset does not contain a separate brand column, so the analysis focuses on the available category hierarchy instead of inventing brand values.

### 05_seller_analysis.py

Analyzes:

- Seller product count
- Seller ratings
- Product ratings
- Average selling price
- Average discounts
- Top sellers
- Highly rated sellers
- Sellers with high discounts

### 06_export_powerbi.py

Creates Power BI-ready CSV files:

- PowerBI_Flipkart_Products.csv
- PowerBI_Category_Summary.csv
- PowerBI_Seller_Summary.csv
- PowerBI_Price_Category_Summary.csv
- PowerBI_Discount_Summary.csv
- PowerBI_KPI_Summary.csv

---

# 🗄️ SQL Analysis

MySQL is used to perform business analysis.

### Basic Analysis

Examples:

```sql
SELECT COUNT(*) AS total_products
FROM products;
```

```sql
SELECT COUNT(DISTINCT seller_name) AS total_sellers
FROM products;
```

### Category Analysis

```sql
SELECT
    category_1,
    COUNT(*) AS product_count,
    ROUND(AVG(product_rating), 2) AS average_rating
FROM products
GROUP BY category_1
ORDER BY product_count DESC;
```

### Pricing Analysis

```sql
SELECT
    category_1,
    ROUND(AVG(selling_price), 2) AS average_price,
    ROUND(AVG(discount_percentage), 2) AS average_discount
FROM products
GROUP BY category_1
ORDER BY average_price DESC;
```

### Seller Analysis

```sql
SELECT
    seller_name,
    COUNT(*) AS product_count,
    ROUND(AVG(seller_rating), 2) AS average_rating
FROM products
GROUP BY seller_name
ORDER BY product_count DESC
LIMIT 10;
```

---

# 📊 Power BI Dashboard

The Power BI dashboard is designed around three main analytical areas.

## Page 1 — Executive Overview

KPIs:

- Total Products
- Total Sellers
- Total Categories
- Average Selling Price
- Average Product Rating
- Average Discount

Visuals:

- Products by Category
- Top 10 Sellers
- Category distribution
- Interactive slicers

---

## Page 2 — Pricing & Discount Analysis

Visuals include:

- MRP vs Selling Price
- Discount percentage distribution
- Average discount by category
- Price category distribution
- Highest-discount products
- Discount category analysis

---

## Page 3 — Seller & Product Analysis

Visuals include:

- Top sellers
- Seller rating comparison
- Product rating comparison
- Average seller price
- Seller discount analysis
- Category and subcategory analysis

---

# 🔍 Key Business Insights

The analysis can be used to identify:

### Product opportunities

Products with:

- High ratings
- Competitive selling prices
- Attractive discounts

can be considered strong-value products.

### Category opportunities

Categories with:

- High product concentration
- High ratings
- Strong discounts

can be evaluated for promotional opportunities.

### Seller performance

Sellers can be compared based on:

- Number of products
- Seller rating
- Product rating
- Average price
- Average discount

---

# 🚀 How to Run the Project

## Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/flipkart-ecommerce-product-pricing-analytics.git
```

```bash
cd flipkart-ecommerce-product-pricing-analytics
```

## Step 2 — Install Python libraries

```bash
pip install -r requirements.txt
```

## Step 3 — Place the dataset

Put the downloaded CSV inside:

```text
data/
```

Rename it if necessary to:

```text
flipkart_products.csv
```

## Step 4 — Run Python files

Run them in this order:

```bash
python python/01_load_and_clean.py
python python/02_eda.py
python python/03_pricing_analysis.py
python python/04_brand_category_analysis.py
python python/05_seller_analysis.py
python python/06_export_powerbi.py
```

## Step 5 — SQL

Open MySQL Workbench and execute:

```text
sql/01_create_table.sql
sql/02_basic_analysis.sql
sql/03_pricing_analysis.sql
sql/04_category_analysis.sql
sql/05_seller_analysis.sql
sql/06_business_insights.sql
```

## Step 6 — Power BI

Open:

```text
powerbi/Flipkart_Ecommerce_Analytics.pbix
```

or import:

```text
output/PowerBI_Flipkart_Products.csv
```

into Power BI and build the dashboard.

---

# 📈 Skills Demonstrated

This project demonstrates:

- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Python
- Pandas
- SQL
- MySQL
- Power BI
- DAX
- KPI Development
- E-Commerce Analytics
- Pricing Analytics
- Seller Analytics
- Category Analysis
- Business Insight Generation

---

# 👨‍💻 Author

**Likith Yadav**

B.Tech Student | Data Analyst Aspirant

Skills:

**Python | SQL | Power BI | Excel | Data Analysis**

---

## ⭐ Project Highlights

**Python → Clean & Analyze**

**SQL → Query & Discover**

**Power BI → Visualize**

**Business Analysis → Recommend**

---

## 📌 Disclaimer

This project is created for educational and portfolio purposes using publicly available product-level data. It is not an official Flipkart analytics system and should not be interpreted as representing Flipkart's internal business data.
