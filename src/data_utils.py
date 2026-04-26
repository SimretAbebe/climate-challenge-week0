import pandas as pd
import numpy as np
from scipy import stats

def clean_climate_data(df):
    """
    Standard cleaning pipeline for NASA POWER climate data.
    1. Replaces NASA sentinel values (-999) with NaN.
    2. Removes duplicate rows.
    3. Performs forward-fill for weather variables to handle missingness.
    """
    # Replace NASA sentinel values
    df = df.replace(-999, np.nan)
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Forward-fill to ensure continuity in time-series
    df = df.ffill()
    
    return df

def detect_outliers(df, columns):
    """
    Computes Z-scores for specified columns and identifies rows where |Z| > 3.
    Returns:
        outliers_df (DataFrame): The subset of data containing outliers.
        count (int): Total number of rows flagged as outliers.
    """
    # Filter numeric columns for safety
    numeric_cols = df[columns].select_dtypes(include=[np.number]).columns
    
    # Compute absolute Z-scores
    z_scores = np.abs(stats.zscore(df[numeric_cols]))
    
    # Flag rows where any column has |Z| > 3
    outliers_mask = (z_scores > 3).any(axis=1)
    outliers_df = df[outliers_mask]
    
    return outliers_df, len(outliers_df)
