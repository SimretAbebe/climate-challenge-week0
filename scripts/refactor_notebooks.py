import json
import os

def update_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            nb = json.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return

    updated = False
    for cell in nb['cells']:
        # Update Imports Cell
        if cell['cell_type'] == 'code' and 'os.environ.pop' in ''.join(cell['source']):
            cell['source'] = [
                "import os\n",
                "import sys\n",
                "\n",
                "# Step 1: Immediately clear the broken setting BEFORE any other imports\n",
                "os.environ.pop('MPLBACKEND', None)\n",
                "\n",
                "# Add the parent directory to the path so we can import from 'src'\n",
                "sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))\n",
                "\n",
                "%matplotlib inline\n",
                "\n",
                "# Step 2: Now it is safe to import the libraries\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "from scipy import stats\n",
                "\n",
                "# Import central utility functions\n",
                "from src.data_utils import clean_climate_data, detect_outliers\n",
                "\n",
                "# Step 3: Professional styling\n",
                "sns.set_theme(style=\"whitegrid\")\n",
                "plt.rcParams['figure.figsize'] = (15, 6)\n",
                "\n",
                "print(\"Environment ready: Libraries loaded safely and modular functions imported.\")"
            ]
            updated = True
        
        # Update Cleaning Cell
        if cell['cell_type'] == 'code' and ("df.replace(-999" in ''.join(cell['source']) or "df.replace(-999" in str(cell['source'])):
             cell['source'] = [
                "# Clean the data using the central utility function\n",
                "df = clean_climate_data(df)\n",
                "\n",
                "# Create the specific variable name used in the plotting code for safety\n",
                "df_cleaned = df\n",
                "\n",
                "print(\"Missing values per column (after modular cleaning):\")\n",
                "print(df_cleaned.isnull().sum())"
            ]
             updated = True

        # Update Outlier Cell
        if cell['cell_type'] == 'code' and ("stats.zscore(df" in ''.join(cell['source']) or "zscore" in ''.join(cell['source'])):
            if "Total rows with outliers" in ''.join(cell['source']):
                cell['source'] = [
                    "# Detect outliers using the central utility function\n",
                    "cols_to_check = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M', 'WS2M_MAX']\n",
                    "outliers_df, count = detect_outliers(df, cols_to_check)\n",
                    "\n",
                    "print(f\"Total rows with outliers (Z > 3): {count}\")\n",
                    "outliers_df.head()"
                ]
                updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"Successfully updated {filepath}")
    else:
        print(f"No matching cells found in {filepath}")

if __name__ == "__main__":
    notebook_dir = 'notebooks'
    for filename in os.listdir(notebook_dir):
        if filename.endswith('.ipynb'):
            update_notebook(os.path.join(notebook_dir, filename))
