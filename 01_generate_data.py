import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

# ==========================================================
# CONFIGURATION
# ==========================================================

total_users = 100000

countries = [
    "India",
    "USA",
    "Australia"
]

states_india = [
    "West Bengal",
    "Karnataka",
    "Maharashtra",
    "Delhi",
    "Tamil Nadu",
    "Kerala",
    "Telangana",
    "Gujarat",
    "Punjab",
    "Odisha",
    "Assam",
    "Sikkim",
    "Uttarakhand",
    "Chhattisgarh",
    "Rajasthan",
    "Uttar Pradesh",
    "Andhra Pradesh",
    "Bihar",
    "Jharkhand"
]

devices = [
    "Desktop",
    "Mobile",
    "Tablet"
]

browsers = [
    "Chrome",
    "Firefox",
    "Safari",
    "Edge"
]

traffic_sources = [
    "Google",
    "Facebook",
    "Instagram",
    "LinkedIn",
    "Email",
    "Referral",
    "Direct"
]

genders = [
    "Male",
    "Female"
]

# ==========================================================
# OUTPUT FOLDER
# ==========================================================

current_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(current_folder)
dataset_folder = os.path.join(project_folder, "Dataset")

# ==========================================================
# DIMENSION TABLES
# ==========================================================

dim_user = []

dim_device = [
    [1, "Desktop"],
    [2, "Mobile"],
    [3, "Tablet"]
]

# ==========================================================
# CREATE USER DIMENSION
# ==========================================================

for user_id in range(1, total_users + 1):

    user_name = fake.name()

    age = np.random.randint(18, 60)

    gender = random.choice(genders)

    country = random.choice(countries)

    if country == "India":
        state = random.choice(states_india)
    else:
        state = fake.state()

    dim_user.append([
        user_id,
        user_name,
        age,
        gender,
        country,
        state
    ])

# ==========================================================
# USER DATAFRAME
# ==========================================================

dim_user_df = pd.DataFrame(
    dim_user,
    columns=[
        "UserID",
        "UserName",
        "Age",
        "Gender",
        "Country",
        "State"
    ]
)

# ==========================================================
# DEVICE DATAFRAME
# ==========================================================

dim_device_df = pd.DataFrame(
    dim_device,
    columns=[
        "DeviceID",
        "DeviceName"
    ]
)

# ==========================================================
# SAVE CSV FILES
# ==========================================================

user_path = os.path.join(dataset_folder, "dim_user.csv")
device_path = os.path.join(dataset_folder, "dim_device.csv")

dim_user_df.to_csv(user_path, index=False)
dim_device_df.to_csv(device_path, index=False)

print("dim_user.csv created")
print(dim_user_df.head())

print()

print("dim_device.csv created")
print(dim_device_df)