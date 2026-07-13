import pandas as pd
import os

# ==========================================================
# Project Folder Setup
# ==========================================================

current_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(current_folder)
dataset_folder = os.path.join(project_folder, "Dataset")

os.makedirs(dataset_folder, exist_ok=True)

# ==========================================================
# Browser Dimension
# ==========================================================

browser_data = [

    [1, "Chrome"],
    [2, "Firefox"],
    [3, "Safari"],
    [4, "Edge"],
    [5, "Opera"]

]

browser_df = pd.DataFrame(

    browser_data,

    columns=[
        "BrowserID",
        "BrowserName"
    ]

)

# ==========================================================
# Save CSV
# ==========================================================

output_file = os.path.join(dataset_folder, "dim_browser.csv")

browser_df.to_csv(output_file, index=False)

print("="*60)
print("Browser Dimension Created Successfully")
print("="*60)

print(browser_df)