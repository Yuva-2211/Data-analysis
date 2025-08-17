import pandas as pd
import numpy as np

# Perform data cleaning and preprocessing on the input DataFrame.
#     Parameters:
#     df (pd.DataFrame): Input DataFrame

#     Returns:
#     pd.DataFrame: Cleaned and preprocessed DataFrame



def clean_df(df: pd.DataFrame):
    """
    Perform data cleaning and preprocessing on the input DataFrame.

    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame
    """
    df = df.copy()  # Fixed

# standardise the column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
    print(f"standardised column names")

# remove duplicates
    d_count = df.duplicated().sum()

    if d_count > 0:
        df.drop_duplicates(inplace=True)
        
#trim and lowercase all objects
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip().str.lower()

    print(f"Standardized string columns (lower case)")

#handling null values    
    null_holder = ["n/a", "na", "--", "-", "none", "null", "", "nan"]
    df.replace(null_holder, np.nan, inplace=True)
    null_report = df.isnull().sum()
    null_report = null_report[null_report > 0]  # Fixed
    if not null_report.empty:
        print(f"Missing values found in df , {null_report}")


#flag constant columns    
    constant_cols = [col for col in df.columns if df[col].nunique() == 1]
    if constant_cols:
        print(f"Constant columns (consider removing): {constant_cols}")

    # Flag high cardinality categorical columns
    high_card_cols = [col for col in df.select_dtypes(include='object') if df[col].nunique() > 100]
    if high_card_cols:
        print(f"High-cardinality columns (consider encoding strategies): {high_card_cols}")

    # Detect numeric outliers using IQR
    num_cols = df.select_dtypes(include=np.number).columns
    outlier_report = {}
    for col in num_cols:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = df[(df[col] < lower) | (df[col] > upper)][col].count()
        if outliers > 0:
            outlier_report[col] = outliers
    if outlier_report:
        print(f"Potential numeric outliers detected:\n{outlier_report}")

    # Convert applicable columns to category
    for col in df.select_dtypes(include='object'):
        n_unique = df[col].nunique()
        if n_unique < len(df) * 0.05:
            df[col] = df[col].astype('category')
    print("Converted suitable object columns to category dtype.")

    print("Data cleaning complete.")
    return df

# Example usage
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5,"nan"],
    'B': ['a', 'b', 'c', 'd', 'e',"--"],
    'C': [1.0, 1.0, 1.0, 1.0, 1.0,1.0]
})
cleaned_df = clean_df(df)  



# Standardizes column names.
# Removes duplicate rows.
# Cleans string/object columns (trims and lowercases).
# Replaces common null-like values with np.nan.
# Reports missing values.
# Flags constant columns and high-cardinality categorical columns.
# Detects numeric outliers using IQR.
# Converts suitable object columns to category dtype.