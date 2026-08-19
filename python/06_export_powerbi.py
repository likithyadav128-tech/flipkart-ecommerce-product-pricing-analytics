import pandas as pd
import os


# ============================================================
# 1. File paths
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\pricing_analysis.csv"

OUTPUT_FOLDER = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output"


# ============================================================
# 2. Create output folder if needed
# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ============================================================
# 3. Load dataset
# ============================================================

print("Loading Flipkart dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")
print("Rows:", len(df))


# ============================================================
# 4. Clean column names
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
)


print("\nAvailable columns:")
print(df.columns.tolist())


# ============================================================
# 5. Select useful Power BI columns
# ============================================================

powerbi_columns = [
    "category_1",
    "category_2",
    "category_3",
    "title",
    "product_rating",
    "selling_price",
    "mrp",
    "seller_name",
    "seller_rating",
    "discount_amount",
    "discount_percentage",
    "price_category",
    "discount_category"
]


# Keep only columns that actually exist

available_columns = [
    column
    for column in powerbi_columns
    if column in df.columns
]


powerbi_products = df[available_columns].copy()


# ============================================================
# 6. Remove duplicate products
# ============================================================

powerbi_products = (
    powerbi_products
    .drop_duplicates()
)


# ============================================================
# 7. Clean numerical columns
# ============================================================

numeric_columns = [
    "product_rating",
    "selling_price",
    "mrp",
    "seller_rating",
    "discount_amount",
    "discount_percentage"
]


for column in numeric_columns:

    if column in powerbi_products.columns:

        powerbi_products[column] = pd.to_numeric(
            powerbi_products[column],
            errors="coerce"
        )


# ============================================================
# 8. Create Product ID
# ============================================================

powerbi_products.insert(
    0,
    "product_id",
    range(
        1,
        len(powerbi_products) + 1
    )
)


# ============================================================
# 9. Export main Power BI file
# ============================================================

main_file = (
    OUTPUT_FOLDER
    + r"\PowerBI_Flipkart_Products.csv"
)


powerbi_products.to_csv(
    main_file,
    index=False
)


print("\nMain Power BI file created:")
print(main_file)


# ============================================================
# 10. Category Summary
# ============================================================

if "category_1" in powerbi_products.columns:

    category_summary = (
        powerbi_products
        .groupby("category_1")
        .agg(
            Product_Count=("product_id", "count"),
            Average_Selling_Price=("selling_price", "mean"),
            Average_MRP=("mrp", "mean"),
            Average_Rating=("product_rating", "mean"),
            Average_Discount=("discount_percentage", "mean")
        )
        .reset_index()
    )


    category_summary.to_csv(
        OUTPUT_FOLDER
        + r"\PowerBI_Category_Summary.csv",
        index=False
    )


# ============================================================
# 11. Seller Summary
# ============================================================

if "seller_name" in powerbi_products.columns:

    seller_summary = (
        powerbi_products
        .groupby("seller_name")
        .agg(
            Product_Count=("product_id", "count"),
            Average_Seller_Rating=("seller_rating", "mean"),
            Average_Product_Rating=("product_rating", "mean"),
            Average_Selling_Price=("selling_price", "mean"),
            Average_Discount=("discount_percentage", "mean")
        )
        .reset_index()
    )


    seller_summary.to_csv(
        OUTPUT_FOLDER
        + r"\PowerBI_Seller_Summary.csv",
        index=False
    )


# ============================================================
# 12. Price Category Summary
# ============================================================

if "price_category" in powerbi_products.columns:

    price_summary = (
        powerbi_products
        .groupby("price_category")
        .agg(
            Product_Count=("product_id", "count"),
            Average_Rating=("product_rating", "mean"),
            Average_Discount=("discount_percentage", "mean")
        )
        .reset_index()
    )


    price_summary.to_csv(
        OUTPUT_FOLDER
        + r"\PowerBI_Price_Category_Summary.csv",
        index=False
    )


# ============================================================
# 13. Discount Category Summary
# ============================================================

if "discount_category" in powerbi_products.columns:

    discount_summary = (
        powerbi_products
        .groupby("discount_category")
        .agg(
            Product_Count=("product_id", "count"),
            Average_Selling_Price=("selling_price", "mean"),
            Average_Rating=("product_rating", "mean")
        )
        .reset_index()
    )


    discount_summary.to_csv(
        OUTPUT_FOLDER
        + r"\PowerBI_Discount_Summary.csv",
        index=False
    )


# ============================================================
# 14. Dashboard KPI Summary
# ============================================================

kpi_data = {
    "KPI": [
        "Total Products",
        "Total Sellers",
        "Total Categories",
        "Average Selling Price",
        "Average MRP",
        "Average Product Rating",
        "Average Seller Rating",
        "Average Discount Percentage"
    ],

    "Value": [
        len(powerbi_products),

        powerbi_products["seller_name"].nunique()
        if "seller_name" in powerbi_products.columns
        else 0,

        powerbi_products["category_1"].nunique()
        if "category_1" in powerbi_products.columns
        else 0,

        powerbi_products["selling_price"].mean()
        if "selling_price" in powerbi_products.columns
        else 0,

        powerbi_products["mrp"].mean()
        if "mrp" in powerbi_products.columns
        else 0,

        powerbi_products["product_rating"].mean()
        if "product_rating" in powerbi_products.columns
        else 0,

        powerbi_products["seller_rating"].mean()
        if "seller_rating" in powerbi_products.columns
        else 0,

        powerbi_products["discount_percentage"].mean()
        if "discount_percentage" in powerbi_products.columns
        else 0
    ]
}


kpi_summary = pd.DataFrame(kpi_data)


kpi_summary.to_csv(
    OUTPUT_FOLDER
    + r"\PowerBI_KPI_Summary.csv",
    index=False
)


# ============================================================
# 15. Final message
# ============================================================

print("\n==========================================")
print("       POWER BI EXPORT COMPLETED")
print("==========================================")

print("""
Power BI files created:

1. PowerBI_Flipkart_Products.csv
2. PowerBI_Category_Summary.csv
3. PowerBI_Seller_Summary.csv
4. PowerBI_Price_Category_Summary.csv
5. PowerBI_Discount_Summary.csv
6. PowerBI_KPI_Summary.csv
""")

print("\nAll files are saved in:")
print(OUTPUT_FOLDER)