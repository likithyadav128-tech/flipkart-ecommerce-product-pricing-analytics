import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. File paths
# ============================================================

INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\cleaned_flipkart_products.csv"

OUTPUT_FOLDER = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output"


# ============================================================
# 2. Load cleaned dataset
# ============================================================

print("Loading cleaned Flipkart dataset...")

df = pd.read_csv(INPUT_FILE)

print("Dataset loaded successfully!")
print("Rows:", len(df))


# ============================================================
# 3. Find price columns
# ============================================================

selling_price = None
mrp = None

for column in df.columns:

    if "selling" in column and "price" in column:
        selling_price = column

    if column == "mrp":
        mrp = column


print("\nSelling Price Column:", selling_price)
print("MRP Column:", mrp)


# ============================================================
# 4. Check required columns
# ============================================================

if selling_price is None or mrp is None:

    print("\nERROR: Price columns were not found.")

    print("Available columns:")
    print(df.columns.tolist())

    raise SystemExit


# ============================================================
# 5. Calculate Discount Amount
# ============================================================

df["discount_amount"] = (
    df[mrp] - df[selling_price]
)


# ============================================================
# 6. Calculate Discount Percentage
# ============================================================

df["discount_percentage"] = (
    df["discount_amount"]
    / df[mrp]
) * 100


# ============================================================
# 7. Remove invalid discount values
# ============================================================

df = df[
    df["discount_percentage"] >= 0
]


# ============================================================
# 8. Pricing Summary
# ============================================================

print("\n==========================================")
print("           PRICING ANALYSIS")
print("==========================================")

print(
    "\nAverage MRP:",
    round(df[mrp].mean(), 2)
)

print(
    "Average Selling Price:",
    round(df[selling_price].mean(), 2)
)

print(
    "Average Discount Amount:",
    round(df["discount_amount"].mean(), 2)
)

print(
    "Average Discount Percentage:",
    round(df["discount_percentage"].mean(), 2),
    "%"
)

print(
    "Maximum Discount Percentage:",
    round(df["discount_percentage"].max(), 2),
    "%"
)


# ============================================================
# 9. Highest Discount Products
# ============================================================

top_discount_products = (
    df.sort_values(
        "discount_percentage",
        ascending=False
    )
    .head(10)
)


print("\n==========================================")
print("       TOP 10 DISCOUNTED PRODUCTS")
print("==========================================")

print(
    top_discount_products[
        [
            "title",
            mrp,
            selling_price,
            "discount_percentage"
        ]
    ]
)


# ============================================================
# 10. Save Top Discount Products
# ============================================================

top_discount_products.to_csv(
    OUTPUT_FOLDER + r"\top_discounted_products.csv",
    index=False
)


# ============================================================
# 11. Create Discount Categories
# ============================================================

def discount_category(discount):

    if discount < 10:
        return "Low Discount"

    elif discount < 30:
        return "Medium Discount"

    elif discount < 50:
        return "High Discount"

    else:
        return "Very High Discount"


df["discount_category"] = (
    df["discount_percentage"]
    .apply(discount_category)
)


# ============================================================
# 12. Discount Category Analysis
# ============================================================

discount_summary = (
    df["discount_category"]
    .value_counts()
    .reset_index()
)

discount_summary.columns = [
    "Discount Category",
    "Number of Products"
]


print("\n==========================================")
print("       DISCOUNT CATEGORY ANALYSIS")
print("==========================================")

print(discount_summary)


# ============================================================
# 13. Save Discount Summary
# ============================================================

discount_summary.to_csv(
    OUTPUT_FOLDER + r"\discount_category_analysis.csv",
    index=False
)


# ============================================================
# 14. Discount Distribution Chart
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["discount_percentage"],
    bins=20
)

plt.title(
    "Flipkart Discount Percentage Distribution"
)

plt.xlabel(
    "Discount Percentage (%)"
)

plt.ylabel(
    "Number of Products"
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    OUTPUT_FOLDER + r"\discount_distribution.png",
    dpi=200
)

plt.show()


# ============================================================
# 15. Price Comparison Chart
# ============================================================

average_prices = pd.DataFrame({
    "Price Type": [
        "MRP",
        "Selling Price"
    ],
    "Average Price": [
        df[mrp].mean(),
        df[selling_price].mean()
    ]
})


plt.figure(figsize=(8, 6))

plt.bar(
    average_prices["Price Type"],
    average_prices["Average Price"]
)

plt.title(
    "Average MRP vs Selling Price"
)

plt.xlabel(
    "Price Type"
)

plt.ylabel(
    "Average Price"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_FOLDER + r"\mrp_vs_selling_price.png",
    dpi=200
)

plt.show()


# ============================================================
# 16. Save Updated Pricing Dataset
# ============================================================

df.to_csv(
    OUTPUT_FOLDER + r"\pricing_analysis.csv",
    index=False
)


# ============================================================
# 17. Final Message
# ============================================================

print("\n==========================================")
print("      PRICING ANALYSIS COMPLETED")
print("==========================================")

print("""
Created files:

1. pricing_analysis.csv
2. top_discounted_products.csv
3. discount_category_analysis.csv
4. discount_distribution.png
5. mrp_vs_selling_price.png
""")