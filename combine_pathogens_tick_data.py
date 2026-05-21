from pathlib import Path
import pandas as pd

source_folder = Path("NEON_pathogens-tick")
output_folder = Path("NEON_pathogens-tick-cleaned")

output_folder.mkdir(exist_ok=True)

all_dataframes = []

for csv_file in source_folder.rglob("*.csv"):
    name = csv_file.name

    if ".tck_pathogen." in name:
        try:
            df = pd.read_csv(csv_file)

            # Keep track of source file
            df["source_file"] = csv_file.name

            all_dataframes.append(df)

            print(f"Loaded: {csv_file}")

        except Exception as e:
            print(f"Failed to read {csv_file}: {e}")

combined_df = pd.concat(all_dataframes, ignore_index=True)

output_file = output_folder / "combined_tck_pathogen_data.csv"
combined_df.to_csv(output_file, index=False)

print(f"\nSaved combined CSV to: {output_file}")
print(f"Total rows: {len(combined_df)}")