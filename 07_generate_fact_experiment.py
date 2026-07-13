import pandas as pd
import numpy as np
import random
import os

# ==========================================================
# Project Folder Setup
# ==========================================================

current_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(current_folder)
dataset_folder = os.path.join(project_folder, "Dataset")

# ==========================================================
# Load Dimension Tables
# ==========================================================

users = pd.read_csv(os.path.join(dataset_folder, "dim_user.csv"))
devices = pd.read_csv(os.path.join(dataset_folder, "dim_device.csv"))
browsers = pd.read_csv(os.path.join(dataset_folder, "dim_browser.csv"))
traffic = pd.read_csv(os.path.join(dataset_folder, "dim_traffic_source.csv"))
dates = pd.read_csv(os.path.join(dataset_folder, "dim_date.csv"))
experiments = pd.read_csv(os.path.join(dataset_folder, "dim_experiment.csv"))

random.seed(42)
np.random.seed(42)

num_records = 100000

fact_rows = []

for fact_id in range(1, num_records + 1):

    user_id = random.randint(1, len(users))
    device_id = random.randint(1, len(devices))
    browser_id = random.randint(1, len(browsers))
    traffic_id = random.randint(1, len(traffic))
    date_id = random.randint(1, len(dates))

    experiment_id = random.choices(
        [1, 2],
        weights=[50, 50],
        k=1
    )[0]

    session_duration = round(np.random.normal(8, 3), 2)
    session_duration = max(session_duration, 1)

    pages_viewed = max(1, int(np.random.normal(6, 2)))

    if experiment_id == 1:
        click_prob = 0.25
        cart_prob = 0.45
        purchase_prob = 0.42
    else:
        click_prob = 0.32
        cart_prob = 0.50
        purchase_prob = 0.47

    clicked = 1 if random.random() < click_prob else 0

    if clicked:
        cart = 1 if random.random() < cart_prob else 0
    else:
        cart = 0

    if cart:
        purchased = 1 if random.random() < purchase_prob else 0
    else:
        purchased = 0

    revenue = 0.0

    if purchased:
        if experiment_id == 1:
            revenue = round(np.random.normal(200, 60), 2)
        else:
            revenue = round(np.random.normal(280, 70), 2)

        revenue = max(revenue, 20)

    fact_rows.append([
        fact_id,
        user_id,
        device_id,
        browser_id,
        traffic_id,
        date_id,
        experiment_id,
        session_duration,
        pages_viewed,
        clicked,
        cart,
        purchased,
        revenue
    ])

fact_df = pd.DataFrame(
    fact_rows,
    columns=[
        "FactID",
        "UserID",
        "DeviceID",
        "BrowserID",
        "TrafficSourceID",
        "DateID",
        "ExperimentID",
        "SessionDuration",
        "PagesViewed",
        "ClickedCTA",
        "AddedToCart",
        "Purchased",
        "Revenue"
    ]
)

output_file = os.path.join(dataset_folder, "fact_experiment.csv")
fact_df.to_csv(output_file, index=False)

print("=" * 60)
print("Fact Table Created Successfully")
print("=" * 60)
print(fact_df.head())
print()
print("Total Records:", len(fact_df))
