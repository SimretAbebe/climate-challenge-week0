import pandas as pd
import os

def load_all_data():
    """Loads all 5 regional datasets from the data/processed folder."""
    countries = ['ethiopia', 'nigeria', 'sudan', 'kenya', 'tanzania']
    all_data = []
    base_path = "data/processed/" 
    
    for c in countries:
        path = os.path.join(base_path, f"{c}_clean.csv")
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['Country'] = c.capitalize()
            all_data.append(df)
            
    if not all_data:
        return pd.DataFrame()
        
    df_all = pd.concat(all_data, ignore_index=True)
    df_all['Date'] = pd.to_datetime(df_all['Date'])
    df_all['Year'] = df_all['Date'].dt.year
    return df_all
