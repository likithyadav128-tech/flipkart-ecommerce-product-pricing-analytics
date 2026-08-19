import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. File paths
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\pricing_analysis.csv"

OUTPUT_FOLDER = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output"


# ============================================================
# 2. Load dataset
# ============================================================

print("Loading Flipkart dataset...")

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Rows:", len(df))


# ============================================================
# 3. Actual columns
# ============================================================

seller = "seller_name"
seller_rating = "seller_rating"
price = "selling_price"
product_rating = "product_rating"
discount = "discount_percentage"


# ============================================================
# 4. Clean seller data
# ============================================================

df[seller] = df[seller].fillna("Unknown")

df[seller] = df[seller].astype(str).str.strip()

df = df[df[seller] != ""]

df[seller_rating] = pd.to_numeric(
    df[seller_rating],
    errors="coerce"
)

df[price] = pd.to_numeric(
    df[price],
    errors="coerce"
)

df[product_rating] = pd.to_numeric(
    df[product_rating],
    errors="coerce"
)

df[discount] = pd.to_numeric(
    df[discount],
    errors="coerce"
)


# ============================================================
# 5. Seller Performance Analysis
# ============================================================

seller_analysis = (
    df.groupby(seller)
    .agg(
        Product_Count=(seller, "count"),
        Average_Seller_Rating=(seller_rating, "mean"),
        Average_Product_Rating=(product_rating, "mean"),
        Average_Selling_Price=(price, "mean"),
        Average_Discount=(discount, "mean")
    )
    .reset_index()
)


# ============================================================
# 6. Sort by number of products
# ============================================================

seller_analysis = (
    seller_analysis
    .sort_values(
        "Product_Count",
        ascending=False
    )
)


print("\n==========================================")
print("SELLER PERFORMANCE ANALYSIS")
print("==========================================")

print(
    seller_analysis.head(20)
)


# ============================================================
# 7. Save complete seller analysis
# ============================================================

seller_analysis.to_csv(
    OUTPUT_FOLDER + r"\seller_analysis.csv",
    index=False
)


# ============================================================
# 8. Top 10 Sellers by Product Count
# ============================================================

top_sellers = (
    seller_analysis
    .head(10)
)


print("\n==========================================")
print("TOP 10 SELLERS BY PRODUCT COUNT")
print("==========================================")

print(top_sellers)


# ============================================================
# 9. Top Seller Chart
# ============================================================

if len(top_sellers) > 0:

    chart_data = (
        top_sellers
        .set_index(seller)["Product_Count"]
        .sort_values()
    )

    plt.figure(figsize=(10, 6))

    chart_data.plot(
        kind="barh"
    )

    plt.title(
        "Top 10 Flipkart Sellers by Product Count"
    )

    plt.xlabel(
        "Number of Products"
    )

    plt.ylabel(
        "Seller"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\top_sellers_product_count.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 10. Top Sellers by Seller Rating
# ============================================================

top_rated_sellers = (
    seller_analysis[
        seller_analysis["Product_Count"] >= 5
    ]
    .sort_values(
        "Average_Seller_Rating",
        ascending=False
    )
    .head(10)
)


print("\n==========================================")
print("TOP RATED SELLERS")
print("==========================================")

print(top_rated_sellers)


# ============================================================
# 11. Save Top Rated Sellers
# ============================================================

top_rated_sellers.to_csv(
    OUTPUT_FOLDER + r"\top_rated_sellers.csv",
    index=False
)


# ============================================================
# 12. Top Rated Seller Chart
# ============================================================

if len(top_rated_sellers) > 0:

    chart_data = (
        top_rated_sellers
        .set_index(seller)["Average_Seller_Rating"]
        .sort_values()
    )

    plt.figure(figsize=(10, 6))

    chart_data.plot(
        kind="barh"
    )

    plt.title(
        "Top Rated Flipkart Sellers"
    )

    plt.xlabel(
        "Average Seller Rating"
    )

    plt.ylabel(
        "Seller"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\top_rated_sellers.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 13. Sellers with Highest Discounts
# ============================================================

top_discount_sellers = (
    seller_analysis[
        seller_analysis["Product_Count"] >= 5
    ]
    .sort_values(
        "Average_Discount",
        ascending=False
    )
    .head(10)
)


print("\n==========================================")
print("SELLERS WITH HIGHEST AVERAGE DISCOUNT")
print("==========================================")

print(top_discount_sellers)


# ============================================================
# 14. Save Discount Sellers
# ============================================================

top_discount_sellers.to_csv(
    OUTPUT_FOLDER + r"\top_discount_sellers.csv",
    index=False
)


# ============================================================
# 15. Discount Seller Chart
# ============================================================

if len(top_discount_sellers) > 0:

    chart_data = (
        top_discount_sellers
        .set_index(seller)["Average_Discount"]
        .sort_values()
    )

    plt.figure(figsize=(10, 6))

    chart_data.plot(
        kind="barh"
    )

    plt.title(
        "Sellers with Highest Average Discounts"
    )

    plt.xlabel(
        "Average Discount (%)"
    )

    plt.ylabel(
        "Seller"
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\top_discount_sellers.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 16. Seller Price Analysis
# ============================================================

top_price_sellers = (
    seller_analysis[
        seller_analysis["Product_Count"] >= 5
    ]
    .sort_values(
        "Average_Selling_Price",
        ascending=False
    )
    .head(10)
)


print("\n==========================================")
print("SELLERS WITH HIGHEST AVERAGE PRICE")
print("==========================================")

print(top_price_sellers)


# ============================================================
# 17. Save Price Sellers
# ============================================================

top_price_sellers.to_csv(
    OUTPUT_FOLDER + r"\top_price_sellers.csv",
    index=False
)


# ============================================================
# 18. Create Seller Performance Category
# ============================================================

def seller_performance(row):

    if (
        row["Average_Seller_Rating"] >= 4.5
        and row["Average_Product_Rating"] >= 4
    ):
        return "Excellent"

    elif (
        row["Average_Seller_Rating"] >= 4
        and row["Average_Product_Rating"] >= 3.5
    ):
        return "Good"

    else:
        return "Needs Improvement"


seller_analysis["Seller_Performance"] = (
    seller_analysis.apply(
        seller_performance,
        axis=1
    )
)


# ============================================================
# 19. Performance Summary
# ============================================================

performance_summary = (
    seller_analysis["Seller_Performance"]
    .value_counts()
    .reset_index()
)


performance_summary.columns = [
    "Performance",
    "Number_of_Sellers"
]


print("\n==========================================")
print("SELLER PERFORMANCE SUMMARY")
print("==========================================")

print(performance_summary)


# ============================================================
# 20. Save Performance Summary
# ============================================================

performance_summary.to_csv(
    OUTPUT_FOLDER + r"\seller_performance_summary.csv",
    index=False
)


# ============================================================
# 21. Final Seller Dataset
# ============================================================

seller_analysis.to_csv(
    OUTPUT_FOLDER + r"\seller_analysis.csv",
    index=False
)


# ============================================================
# 22. Final Message
# ============================================================

print("\n==========================================")
print("SELLER ANALYSIS COMPLETED SUCCESSFULLY")
print("==========================================")

print("""
Created files:

1. seller_analysis.csv
2. top_rated_sellers.csv
3. top_discount_sellers.csv
4. top_price_sellers.csv
5. seller_performance_summary.csv

Charts:

6. top_sellers_product_count.png
7. top_rated_sellers.png
8. top_discount_sellers.png
""")