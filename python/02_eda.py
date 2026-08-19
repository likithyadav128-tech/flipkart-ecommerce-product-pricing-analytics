import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. Load cleaned dataset
# ==========================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\cleaned_flipkart_products.csv"

print("Loading cleaned Flipkart dataset...")

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# 2. Display columns
# ==========================================

print("\n==========================================")
print("AVAILABLE COLUMNS")
print("==========================================")

print(df.columns.tolist())


# ==========================================
# 3. Basic Dataset Information
# ==========================================

print("\n==========================================")
print("DATASET INFORMATION")
print("==========================================")

print(df.info())


# ==========================================
# 4. Missing Values
# ==========================================

print("\n==========================================")
print("MISSING VALUES")
print("==========================================")

print(df.isnull().sum())


# ==========================================
# 5. Find important columns
# ==========================================

price_column = None
rating_column = None
seller_rating_column = None
brand_column = None
category_column = None


for column in df.columns:

    if "selling" in column and "price" in column:
        price_column = column

    if "product" in column and "rating" in column:
        rating_column = column

    if "seller" in column and "rating" in column:
        seller_rating_column = column

    if "brand" in column:
        brand_column = column

    if "category1" in column:
        category_column = column


print("\n==========================================")
print("IMPORTANT COLUMNS")
print("==========================================")

print("Price:", price_column)
print("Product Rating:", rating_column)
print("Seller Rating:", seller_rating_column)
print("Brand:", brand_column)
print("Category:", category_column)


# ==========================================
# 6. Basic Business Metrics
# ==========================================

print("\n==========================================")
print("BUSINESS METRICS")
print("==========================================")


total_products = len(df)


if brand_column:
    total_brands = df[brand_column].nunique()
else:
    total_brands = 0


if category_column:
    total_categories = df[category_column].nunique()
else:
    total_categories = 0


print("Total Products:", total_products)
print("Total Brands:", total_brands)
print("Total Categories:", total_categories)


# ==========================================
# 7. Price Analysis
# ==========================================

if price_column:

    average_price = df[price_column].mean()
    minimum_price = df[price_column].min()
    maximum_price = df[price_column].max()

    print("\n==========================================")
    print("PRICE ANALYSIS")
    print("==========================================")

    print(
        "Average Selling Price:",
        round(average_price, 2)
    )

    print(
        "Minimum Selling Price:",
        round(minimum_price, 2)
    )

    print(
        "Maximum Selling Price:",
        round(maximum_price, 2)
    )


# ==========================================
# 8. Rating Analysis
# ==========================================

if rating_column:

    average_rating = df[rating_column].mean()

    print("\n==========================================")
    print("RATING ANALYSIS")
    print("==========================================")

    print(
        "Average Product Rating:",
        round(average_rating, 2)
    )


if seller_rating_column:

    average_seller_rating = (
        df[seller_rating_column].mean()
    )

    print(
        "Average Seller Rating:",
        round(average_seller_rating, 2)
    )


# ==========================================
# 9. Discount Analysis
# ==========================================

if "discount_percentage" in df.columns:

    average_discount = (
        df["discount_percentage"].mean()
    )

    maximum_discount = (
        df["discount_percentage"].max()
    )

    print("\n==========================================")
    print("DISCOUNT ANALYSIS")
    print("==========================================")

    print(
        "Average Discount:",
        round(average_discount, 2),
        "%"
    )

    print(
        "Maximum Discount:",
        round(maximum_discount, 2),
        "%"
    )


# ==========================================
# 10. Top Brands
# ==========================================

if brand_column:

    top_brands = (
        df[brand_column]
        .value_counts()
        .head(10)
    )

    print("\n==========================================")
    print("TOP 10 BRANDS")
    print("==========================================")

    print(top_brands)

    top_brands.to_csv(
        r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\top_10_brands.csv"
    )


# ==========================================
# 11. Top Categories
# ==========================================

if category_column:

    top_categories = (
        df[category_column]
        .value_counts()
        .head(10)
    )

    print("\n==========================================")
    print("TOP CATEGORIES")
    print("==========================================")

    print(top_categories)

    top_categories.to_csv(
       r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\top_categories.csv"
    )


# ==========================================
# 12. Price Category Analysis
# ==========================================

if "price_category" in df.columns:

    price_categories = (
        df["price_category"]
        .value_counts()
    )

    print("\n==========================================")
    print("PRODUCTS BY PRICE CATEGORY")
    print("==========================================")

    print(price_categories)


# ==========================================
# 13. Product Rating Distribution
# ==========================================

if rating_column:

    plt.figure(figsize=(10, 6))

    plt.hist(
        df[rating_column].dropna(),
        bins=10
    )

    plt.title(
        "Flipkart Product Rating Distribution"
    )

    plt.xlabel("Product Rating")

    plt.ylabel("Number of Products")

    plt.grid(
        True,
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\product_rating_distribution.png",
        dpi=200
    )

    plt.show()


# ==========================================
# 14. Selling Price Distribution
# ==========================================

if price_column:

    plt.figure(figsize=(10, 6))

    plt.hist(
        df[price_column].dropna(),
        bins=30
    )

    plt.title(
        "Flipkart Selling Price Distribution"
    )

    plt.xlabel("Selling Price")

    plt.ylabel("Number of Products")

    plt.grid(
        True,
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\selling_price_distribution.png",
        dpi=200
    )

    plt.show()


# ==========================================
# 15. Final Message
# ==========================================

print("\n==========================================")
print("EDA COMPLETED SUCCESSFULLY")
print("==========================================")

print("""
Created analysis for:

1. Product count
2. Brand count
3. Category count
4. Price analysis
5. Product rating analysis
6. Seller rating analysis
7. Discount analysis
8. Top brands
9. Top categories
10. Price categories
""")