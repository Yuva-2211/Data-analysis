# Data Cleaning Utility 🧹

This repository contains a reusable Python function for **data cleaning and preprocessing** using **pandas** and **numpy**. The function `clean_df()` standardizes and prepares datasets for analysis or modeling.

---

## Features ✨

The `clean_df()` function performs the following steps:

- **Standardize Column Names**  
  Converts column names to lowercase, replaces spaces with underscores, and trims whitespace.  

- **Remove Duplicate Rows**  
  Automatically detects and removes duplicate rows.  

- **Clean String/Object Columns**  
  Trims whitespace and converts all string values to lowercase.  

- **Handle Null Values**  
  Replaces common placeholders (`n/a`, `na`, `--`, `-`, `none`, `null`, `""`, `nan`) with `np.nan`.  
  Reports columns with missing values.  

- **Flag Constant Columns**  
  Detects columns with only one unique value (considered non-informative).  

- **Flag High-Cardinality Categorical Columns**  
  Identifies categorical columns with a large number of unique values (useful for deciding encoding strategies).  

- **Detect Numeric Outliers**  
  Uses the **Interquartile Range (IQR)** method to detect and report outliers in numeric columns.  

- **Convert Columns to Category**  
  Converts object-type columns to categorical if their unique values are less than 5% of the total rows.  

---

## Installation ⚙️

Make sure you have Python 3.x installed along with the required libraries:

```bash
pip install pandas numpy
```

---

## Usage 🚀

```python
import pandas as pd
from cleaner import clean_df   # if saved as cleaner.py

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, "nan"],
    'B': ['a', 'b', 'c', 'd', 'e', "--"],
    'C': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
})

# Clean the DataFrame
cleaned_df = clean_df(df)
print(cleaned_df)
```

---

## Example Output 📊

Running the script will:

- Standardize column names  
- Replace invalid entries with `NaN`  
- Drop duplicates (if any)  
- Flag issues (like missing values, constants, or outliers)  

**Example log:**

```
standardised column names
Standardized string columns (lower case)
Missing values found in df , A    1
Constant columns (consider removing): ['c']
Converted suitable object columns to category dtype.
Data cleaning complete.
```

---

## Notes 📝

- This function **does not impute missing values** (only flags them). You can decide on strategies like mean/median imputation, forward-fill, or model-based imputation depending on your use case.  
- Outliers are reported but not removed automatically.  
- Use this as a **preprocessing step** before feature engineering and model training.  

---

## Author 👨‍💻

Developed by **[Yuva Shankar Narayana](https://www.linkedin.com/in/yuva-shankar-narayana/)**  

---

## License 📜

This project is open-source and available under the **MIT License**.  
