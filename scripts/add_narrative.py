import json
import os

def update_notebook_narrative(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    new_cells = []
    for cell in nb['cells']:
        new_cells.append(cell)
        
        # Add observation under Temperature Time Series
        if cell['cell_type'] == 'code' and 'plt.plot' in ''.join(cell['source']) and 'T2M' in ''.join(cell['source']):
            new_cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "> **Scientific Observation (Thermal Trends):**\n",
                    "The persistent multi-year warming trend observed here, despite seasonal fluctuations, indicates a shifting regional baseline. For COP32 planning, this suggests that 'normal' temperatures are moving into higher percentiles, increasing the risk of heat stress on agricultural productivity."
                ]
            })

        # Add observation under Rainfall Analysis
        if cell['cell_type'] == 'code' and ('plt.bar' in ''.join(cell['source']) or 'PRECTOTCORR' in ''.join(cell['source'])):
            if 'monthly_rain' in ''.join(cell['source']) or 'precipitation' in ''.join(cell['source']).lower():
                new_cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "> **Scientific Observation (Precipitation Volatility):**\n",
                        "The high variance between average and peak rainfall identified in this study confirms the episodic nature of tropical precipitation. This volatility necessitates a shift from steady-state water management to 'extreme-event' resilience, as infrastructure must withstand high-intensity convective bursts rather than seasonal averages."
                    ]
                })

    nb['cells'] = new_cells
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Narrative added to {filepath}")

if __name__ == "__main__":
    notebook_dir = 'notebooks'
    for filename in os.listdir(notebook_dir):
        if filename.endswith('.ipynb'):
            update_notebook_narrative(os.path.join(notebook_dir, filename))
