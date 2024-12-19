import pandas as pd
import numpy as np

def analyze_inventory(df):
    """
    Perform inventory analysis on cleaned data
    """
    # Group by product and warehouse
    inventory_analysis = df.groupby(['product_category', 'warehouse']).agg({
        'order_item_quantity': 'sum',
        'sales': 'sum',
        'delivery_time': 'mean',
        'order_id': 'count'
    }).reset_index()
    
    # Calculate key metrics
    inventory_analysis['avg_order_value'] = inventory_analysis['sales'] / inventory_analysis['order_id']
    inventory_analysis['delivery_efficiency'] = np.where(
        inventory_analysis['delivery_time'] <= 3,
        'Efficient',
        'Needs Improvement'
    )
    
    return inventory_analysis

def calculate_cost_savings(df):
    """
    Calculate potential cost savings
    """
    # Identify excess inventory
    df['excess_stock'] = df.apply(
        lambda x: max(0, x['order_item_quantity'] - (x['order_id'] * 1.5)),
        axis=1
    )
    
    # Calculate potential savings
    df['potential_savings'] = df['excess_stock'] * (df['sales'] / df['order_item_quantity'])
    
    return df

if __name__ == "__main__":
    # Load cleaned data
    df = pd.read_csv('data/processed/cleaned_data.csv')
    
    # Perform analysis
    inventory_results = analyze_inventory(df)
    savings_results = calculate_cost_savings(inventory_results)
    
    # Save results
    savings_results.to_csv('data/processed/inventory_analysis.csv', index=False)
    print(f"Total potential savings identified: ${savings_results['potential_savings'].sum():,.2f}")
