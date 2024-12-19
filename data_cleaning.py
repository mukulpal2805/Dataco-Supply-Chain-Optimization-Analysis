import pandas as pd
import numpy as np

def clean_supply_chain_data(file_path):
    """
    Clean and prepare DataCo supply chain data
    """
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Clean column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Convert dates
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])
    
    # Calculate delivery time
    df['delivery_time'] = (df['shipping_date'] - df['order_date']).dt.days
    
    # Clean and convert numeric columns
    df['order_item_quantity'] = pd.to_numeric(df['order_item_quantity'], errors='coerce')
    df['sales'] = pd.to_numeric(df['sales'], errors='coerce')
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df['order_item_quantity'] = df['order_item_quantity'].fillna(0)
    df['sales'] = df['sales'].fillna(0)
    
    return df

if __name__ == "__main__":
    df = clean_supply_chain_data('data/raw/DataCoSupplyChainDataset.csv')
    df.to_csv('data/processed/cleaned_data.csv', index=False)
    print("Data cleaning completed!")
