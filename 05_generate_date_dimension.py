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
# Generate Date Dimension
# ==========================================================

start_date = "2025-01-01"
end_date = "2026-12-31"

dates = pd.date_range(start=start_date, end=end_date)

date_df = pd.DataFrame()

date_df["DateID"] = range(1, len(dates) + 1)

date_df["Date"] = dates

date_df["Day"] = dates.day

date_df["Month"] = dates.month

date_df["MonthName"] = dates.month_name()

date_df["Quarter"] = "Q" + dates.quarter.astype(str)

date_df["Year"] = dates.year

date_df["Week"] = dates.isocalendar().week.astype(int)

date_df["DayOfWeek"] = dates.dayofweek + 1

date_df["DayName"] = dates.day_name()

date_df["IsWeekend"] = dates.dayofweek >= 5

date_df["IsWeekend"] = date_df["IsWeekend"].map({
    True: "Yes",
    False: "No"
})

# ==========================================================
# Save CSV
# ==========================================================

output_file = os.path.join(
    dataset_folder,
    "dim_date.csv"
)

date_df.to_csv(
    output_file,
    index=False
)

# ==========================================================
# Display
# ==========================================================

print("=" * 60)
print("Date Dimension Created Successfully")
print("=" * 60)

print(date_df.head())

print()

print("Total Dates Generated:", len(date_df))