import json
import os

def update_notebook_paths(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Determine country from filename (e.g., ethiopia_eda.ipynb -> ethiopia)
    country = os.path.basename(filepath).split('_')[0]

    updated = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source_str = ''.join(cell['source'])
            
            # 1. Update Loading Path: ../data/ethiopia.csv -> ../data/raw/ethiopia.csv
            if f"pd.read_csv('../data/{country}.csv')" in source_str:
                cell['source'] = [line.replace(f"../data/{country}.csv", f"../data/raw/{country}.csv") for line in cell['source']]
                updated = True
                
            # 2. Update Export Path: ../data/ethiopia_clean.csv -> ../data/processed/ethiopia_clean.csv
            if f"../data/{country}_clean.csv" in source_str:
                cell['source'] = [line.replace(f"../data/{country}_clean.csv", f"../data/processed/{country}_clean.csv") for line in cell['source']]
                updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"Paths updated in {filepath}")
    else:
        print(f"No paths needed updating in {filepath}")

if __name__ == "__main__":
    notebook_dir = 'notebooks'
    for filename in os.listdir(notebook_dir):
        if filename.endswith('.ipynb'):
            update_notebook_paths(os.path.join(notebook_dir, filename))
