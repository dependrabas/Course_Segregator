import pandas as pd
import os

PROGRAMMES = [
    "Bachelor of Arts in Language and Heritage Studies",
    "Bachelor of Arts in History and Global Affairs",
    "Bachelor of Arts in Bhutan Studies and Global Perspectives",
    "Bachelor of Arts in Cultural Innovation and Entrepreneurship",
    "Bachelor of Arts in Psychology and Mindfulness"
]

COLUMN_NAME = "7. Programme Applied For"


def separate_programmes(file_path, output_folder="output"):
    
    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_csv(file_path)

    created_files = []

    for programme in PROGRAMMES:
        # Create a list to store rows for this programme
        programme_rows = []
        
        for idx, row in df.iterrows():
            programmes_in_cell = row[COLUMN_NAME]
            
            # Skip if cell is empty or NaN
            if pd.isna(programmes_in_cell):
                continue
            
            # Split by comma and check if this programme is in the list
            programmes_list = [p.strip() for p in str(programmes_in_cell).split(',')]
            
            if programme in programmes_list:
                # Create a copy of the row and set ONLY this single programme
                row_copy = row.copy()
                row_copy[COLUMN_NAME] = programme  # Set to only this one programme
                programme_rows.append(row_copy)
        
        # Only create file if there are students who applied for this programme
        if len(programme_rows) > 0:
            filtered_df = pd.DataFrame(programme_rows)
            # Create short filename for cleaner output
            short_name = programme.replace("Bachelor of Arts in ", "").replace(" ", "_")
            filename = short_name + ".csv"
            filepath = os.path.join(output_folder, filename)

            filtered_df.to_csv(filepath, index=False)

            created_files.append((short_name.replace("_", " "), filepath))

    return created_files