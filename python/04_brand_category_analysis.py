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
# 3. Actual columns in your dataset
# ============================================================

category_1 = "category_1"
category_2 = "category_2"
category_3 = "category_3"

rating = "product_rating"
price = "selling_price"

seller = "seller_name"
seller_rating = "seller_rating"


# ============================================================
# 4. Remove blank values from important columns
# ============================================================

df[category_1] = df[category_1].fillna("Unknown")
df[category_2] = df[category_2].fillna("Unknown")
df[category_3] = df[category_3].fillna("Unknown")

df[seller] = df[seller].fillna("Unknown")


# Remove completely blank text values

df = df[df[category_1].astype(str).str.strip() != ""]
df = df[df[seller].astype(str).str.strip() != ""]


# ============================================================
# 5. CATEGORY 1 ANALYSIS
# ============================================================

category_analysis = (
    df.groupby(category_1)
    .agg(
        Product_Count=(category_1, "count"),
        Average_Price=(price, "mean"),
        Average_Rating=(rating, "mean"),
        Average_Discount=("discount_percentage", "mean")
    )
    .sort_values(
        "Product_Count",
        ascending=False
    )
    .reset_index()
)


print("\n==========================================")
print("CATEGORY 1 ANALYSIS")
print("==========================================")

print(category_analysis.head(20))


category_analysis.to_csv(
    OUTPUT_FOLDER + r"\category_1_analysis.csv",
    index=False
)


# ============================================================
# 6. CATEGORY 2 ANALYSIS
# ============================================================

category_2_analysis = (
    df.groupby(category_2)
    .agg(
        Product_Count=(category_2, "count"),
        Average_Price=(price, "mean"),
        Average_Rating=(rating, "mean"),
        Average_Discount=("discount_percentage", "mean")
    )
    .sort_values(
        "Product_Count",
        ascending=False
    )
    .reset_index()
)


print("\n==========================================")
print("CATEGORY 2 ANALYSIS")
print("==========================================")

print(category_2_analysis.head(20))


category_2_analysis.to_csv(
    OUTPUT_FOLDER + r"\category_2_analysis.csv",
    index=False
)


# ============================================================
# 7. CATEGORY 3 ANALYSIS
# ============================================================

category_3_analysis = (
    df.groupby(category_3)
    .agg(
        Product_Count=(category_3, "count"),
        Average_Price=(price, "mean"),
        Average_Rating=(rating, "mean"),
        Average_Discount=("discount_percentage", "mean")
    )
    .sort_values(
        "Product_Count",
        ascending=False
    )
    .reset_index()
)


print("\n==========================================")
print("CATEGORY 3 ANALYSIS")
print("==========================================")

print(category_3_analysis.head(20))


category_3_analysis.to_csv(
    OUTPUT_FOLDER + r"\category_3_analysis.csv",
    index=False
)


# ============================================================
# 8. TOP CATEGORIES
# ============================================================

top_categories = (
    df[category_1]
    .value_counts()
    .head(10)
)


print("\n==========================================")
print("TOP 10 CATEGORIES")
print("==========================================")

print(top_categories)


if len(top_categories) > 0:

    plt.figure(figsize=(10, 6))

    top_categories.sort_values().plot(
        kind="barh"
    )

    plt.title("Top 10 Flipkart Categories")
    plt.xlabel("Number of Products")
    plt.ylabel("Category")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\top_categories.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 9. CATEGORY RATING
# ============================================================

category_rating = (
    df.groupby(category_1)[rating]
    .mean()
    .dropna()
    .sort_values(ascending=False)
    .head(10)
)


print("\n==========================================")
print("TOP CATEGORIES BY RATING")
print("==========================================")

print(category_rating)


if len(category_rating) > 0:

    plt.figure(figsize=(10, 6))

    category_rating.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top Categories by Average Product Rating"
    )

    plt.xlabel("Average Product Rating")
    plt.ylabel("Category")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\category_rating.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 10. CATEGORY DISCOUNT
# ============================================================

category_discount = (
    df.groupby(category_1)["discount_percentage"]
    .mean()
    .dropna()
    .sort_values(ascending=False)
    .head(10)
)


print("\n==========================================")
print("TOP CATEGORIES BY DISCOUNT")
print("==========================================")

print(category_discount)


if len(category_discount) > 0:

    plt.figure(figsize=(10, 6))

    category_discount.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top Categories by Average Discount"
    )

    plt.xlabel("Average Discount (%)")
    plt.ylabel("Category")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\category_discount.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 11. CATEGORY PRICE
# ============================================================

category_price = (
    df.groupby(category_1)[price]
    .mean()
    .dropna()
    .sort_values(ascending=False)
    .head(10)
)


print("\n==========================================")
print("TOP CATEGORIES BY PRICE")
print("==========================================")

print(category_price)


if len(category_price) > 0:

    plt.figure(figsize=(10, 6))

    category_price.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top Categories by Average Selling Price"
    )

    plt.xlabel("Average Selling Price")
    plt.ylabel("Category")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_FOLDER + r"\category_price.png",
        dpi=200
    )

    plt.show()

    plt.close()


# ============================================================
# 12. TOP SELLERS
# ============================================================

top_sellers = (
    df[seller]
    .value_counts()
    .head(10)
)


print("\n==========================================")
print("TOP 10 SELLERS")
print("==========================================")

print(top_sellers)


if len(top_sellers) > 0:

    top_sellers.to_csv(
        OUTPUT_FOLDER + r"\top_sellers.csv"
    )


# ============================================================
# 13. FINAL MESSAGE
# ============================================================

print("\n==========================================")
print("CATEGORY ANALYSIS COMPLETED")
print("==========================================")

print("""
Created files:

1. category_1_analysis.csv
2. category_2_analysis.csv
3. category_3_analysis.csv
4. top_categories.png
5. category_rating.png
6. category_discount.png
7. category_price.png
8. top_sellers.csv
""")