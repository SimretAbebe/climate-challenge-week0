import json
import os

def update_notebook_extra_narrative(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    new_cells = []
    for cell in nb['cells']:
        new_cells.append(cell)
        
        # Add observation under Humidity
        if cell['cell_type'] == 'code' and 'RH2M' in ''.join(cell['source']) and ('plt' in ''.join(cell['source']) or 'sns' in ''.join(cell['source'])):
            if 'hist' in ''.join(cell['source']) or 'plot' in ''.join(cell['source']) or 'scatter' in ''.join(cell['source']):
                # Only add if not already added
                source_str = ''.join(cell['source'])
                if 'Scientific Observation (Humidity Dynamics)' not in source_str:
                    new_cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [
                            "> **Scientific Observation (Humidity Dynamics):**\n",
                            "The relative humidity baseline identifies the moisture-holding capacity of the regional atmosphere. High humidity levels combined with rising temperatures increase 'wet-bulb' temperature risks, which is a critical indicator for human health and livestock resilience under future climate scenarios."
                        ]
                    })

        # Add observation under Wind Speed
        if cell['cell_type'] == 'code' and 'WS2M' in ''.join(cell['source']) and ('plt' in ''.join(cell['source']) or 'sns' in ''.join(cell['source'])):
             if 'hist' in ''.join(cell['source']) or 'plot' in ''.join(cell['source']) or 'scatter' in ''.join(cell['source']):
                source_str = ''.join(cell['source'])
                if 'Scientific Observation (Atmospheric Energy)' not in source_str:
                    new_cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [
                            "> **Scientific Observation (Atmospheric Energy):**\n",
                            "The distribution and peaks of wind speed represent the kinetic energy of the regional climate system. Variations in these patterns, especially during extreme rainfall events, suggest an increase in storm energy which has direct implications for the mechanical resilience of energy and communication infrastructure."
                        ]
                    })

    nb['cells'] = new_cells
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print(f"Extra narrative added to {filepath}")

if __name__ == "__main__":
    notebook_dir = 'notebooks'
    for filename in os.listdir(notebook_dir):
        if filename.endswith('.ipynb'):
            update_notebook_extra_narrative(os.path.join(notebook_dir, filename))
