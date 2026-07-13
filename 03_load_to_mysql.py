import pandas as pd
import numpy as np
import os
from mysql_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

current_folder = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.dirname(current_folder)
dataset_folder = os.path.join(project_folder, "Dataset")

tables = [
    ("dim_user", "dim_user.csv"),
    ("dim_device", "dim_device.csv"),
    ("dim_browser", "dim_browser.csv"),
    ("dim_traffic_source", "dim_traffic_source.csv"),
    ("dim_date", "dim_date.csv"),
    ("dim_experiment", "dim_experiment.csv"),
    ("fact_experiment", "fact_experiment.csv")
]

batch_size = 5000

# Clear old data first
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

for table_name, file_name in reversed(tables):
    cursor.execute(f"TRUNCATE TABLE {table_name}")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
connection.commit()

for table_name, file_name in tables:
    file_path = os.path.join(dataset_folder, file_name)

    df = pd.read_csv(file_path)

    # Remove bad unnamed/blank columns
    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]
    df.columns = df.columns.astype(str).str.strip()

    # Replace NaN with None for MySQL NULL
    df = df.replace({np.nan: None})

    columns = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    insert_query = f"""
    INSERT INTO {table_name} ({columns})
    VALUES ({placeholders})
    """

    data = [tuple(row) for row in df.itertuples(index=False, name=None)]

    total_rows = len(data)

    for i in range(0, total_rows, batch_size):
        batch = data[i:i + batch_size]
        cursor.executemany(insert_query, batch)
        connection.commit()

        print(f"{table_name}: inserted rows {i + 1} to {min(i + batch_size, total_rows)}")

    print(f"{table_name} loaded successfully: {total_rows} rows")

cursor.close()
connection.close()

print("All tables loaded successfully!")

