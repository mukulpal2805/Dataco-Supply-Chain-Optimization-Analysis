import pandas as pd

def analyze_supplier_performance(df):
    """
    Analyze supplier delivery performance
    """
    supplier_metrics = df.groupby('supplier').agg({
        'delivery_time': 'mean',
        'order_id': 'count',
        'order_item_quantity': 'sum'
    }).reset_index()
    
    # Calculate performance score
    supplier_metrics['performance_score'] = 100 - (supplier_metrics['delivery_time'] * 5)
    supplier_metrics['performance_category'] = pd.qcut(
        supplier_metrics['performance_score'],
        q=3,
        labels=['Needs Improvement', 'Good', 'Excellent']
    )
    
    return supplier_metrics

if __name__ == "__main__":
    df = pd.read_csv('data/processed/cleaned_data.csv')
    supplier_analysis = analyze_supplier_performance(df)
    supplier_analysis.to_csv('data/processed/supplier_analysis.csv', index=False)
