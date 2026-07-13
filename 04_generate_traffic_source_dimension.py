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
# Traffic Source Dimension
# ==========================================================

traffic_source_data = [

    [1, "Organic Search"],
    [2, "Paid Search"],
    [3, "Direct"],
    [4, "Social Media"],
    [5, "Email"],
    [6, "Referral"]

]

traffic_source_df = pd.DataFrame(

    traffic_source_data,

    columns=[
        "TrafficSourceID",
        "TrafficSourceName"
    ]

)

# ==========================================================
# Save CSV
# ==========================================================

output_file = os.path.join(
    dataset_folder,
    "dim_traffic_source.csv"
)

traffic_source_df.to_csv(
    output_file,
    index=False
)

# ==========================================================
# Display
# ==========================================================

print("=" * 60)
print("Traffic Source Dimension Created Successfully")
print("=" * 60)

print(traffic_source_df)