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
# Experiment Dimension
# ==========================================================

experiment_data = [

    [
        1,
        "A",
        "Current Website",
        "Original Product Page"
    ],

    [
        2,
        "B",
        "New Website",
        "Improved Product Page"
    ]

]

experiment_df = pd.DataFrame(

    experiment_data,

    columns=[

        "ExperimentID",
        "ExperimentGroup",
        "ExperimentName",
        "Description"

    ]

)

# ==========================================================
# Save CSV
# ==========================================================

output_file = os.path.join(
    dataset_folder,
    "dim_experiment.csv"
)

experiment_df.to_csv(
    output_file,
    index=False
)

# ==========================================================
# Display
# ==========================================================

print("=" * 60)
print("Experiment Dimension Created Successfully")
print("=" * 60)

print(experiment_df)