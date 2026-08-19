import pandas as pd

# ==========================================
# 1. File paths
# ==========================================


INPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\dataset\dataset.csv"
OUTPUT_FILE = r"C:\Users\likit\OneDrive\Documents\FLIPKART E-COMMERCE ANALYSIS\output\cleaned_flipkart_products.csv"


# ==========================================
# 2. Load dataset
# ==========================================

print("Loading Flipkart dataset...")

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Shape:", df.shape)


# ==========================================
# 3. Clean column names
# ==========================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n==========================================")
print("ACTUAL COLUMN NAMES")
print("==========================================")

print(df.columns.tolist())


# ==========================================
# 4. Show first rows
# ==========================================

print("\nFirst 5 rows:")
print(df.head())


# ==========================================
# 5. Remove duplicate rows
# ==========================================

print("\nRemoving duplicate rows...")

df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))


# ==========================================
# 6. Check important columns
# ==========================================

print("\nChecking available columns...")

print(df.columns.tolist())


# ==========================================
# 7. Try to identify price columns
# ==========================================

selling_price_column = None
mrp_column = None


for column in df.columns:

    if "selling" in column and "price" in column:
        selling_price_column = column

    if column == "mrp":
        mrp_column = column

    elif "mrp" in column:
        mrp_column = column


print("\nSelling Price column:", selling_price_column)
print("MRP column:", mrp_column)


# ==========================================
# 8. Stop if columns are not found
# ==========================================

if selling_price_column is None:

    print("\nERROR: Selling price column was not found.")

    print("\nAvailable columns are:")
    print(df.columns.tolist())

    print(
        "\nSend me these column names and I will "
        "adjust the code for your dataset."
    )

    raise SystemExit


if mrp_column is None:

    print("\nERROR: MRP column was not found.")

    print("\nAvailable columns are:")
    print(df.columns.tolist())

    raise SystemExit


# ==========================================
# 9. Convert prices to numbers
# ==========================================

df[selling_price_column] = pd.to_numeric(
    df[selling_price_column],
    errors="coerce"
)

df[mrp_column] = pd.to_numeric(
    df[mrp_column],
    errors="coerce"
)


# ==========================================
# 10. Remove invalid prices
# ==========================================

df = df[
    (df[selling_price_column] > 0) &
    (df[mrp_column] > 0)
]


# ==========================================
# 11. Create Discount Amount
# ==========================================

df["discount_amount"] = (
    df[mrp_column]
    - df[selling_price_column]
)


# ==========================================
# 12. Create Discount Percentage
# ==========================================

df["discount_percentage"] = (
    df["discount_amount"]
    / df[mrp_column]
) * 100


# ==========================================
# 13. Create Price Category
# ==========================================

def price_category(price):

    if price < 500:
        return "Under ₹500"

    elif price < 2000:
        return "₹500 - ₹2,000"

    elif price < 5000:
        return "₹2,000 - ₹5,000"

    elif price < 10000:
        return "₹5,000 - ₹10,000"

    else:
        return "Above ₹10,000"


df["price_category"] = (
    df[selling_price_column]
    .apply(price_category)
)


# ==========================================
# 14. Final information
# ==========================================

print("\n==========================================")
print("CLEANED DATA")
print("==========================================")

print("Final shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ==========================================
# 15. Save cleaned dataset
# ==========================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("\n==========================================")
print("CLEANING COMPLETED SUCCESSFULLY")
print("==========================================")

print("Saved file:")
print(OUTPUT_FILE)