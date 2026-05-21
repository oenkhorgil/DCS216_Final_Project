from pathlib import Path
import shutil

source_folder = Path("NEON_count-ticks")
output_folder = Path("NEON_count-ticks-cleaned")

output_folder.mkdir(exist_ok=True)

for csv_file in source_folder.rglob("*.csv"):
    name = csv_file.name

    if ".tck_fielddata." in name or ".tck_taxonomyProcessed." in name:
        destination = output_folder / name

        # Avoid overwriting if duplicate filenames exist
        if destination.exists():
            destination = output_folder / f"{csv_file.parent.name}_{name}"

        shutil.copy2(csv_file, destination)
        print(f"Copied: {csv_file} -> {destination}")

print("Done.")