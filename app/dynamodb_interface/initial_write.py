from db_utils.dynamodb_writer import DynamodbWriter
import pandas as pd
from decimal import Decimal

def load_csv_data():
    items_df = pd.read_csv('data/initial_food_stats_per_kg.csv')
    float_cols = ['g_protein_per_kg','kcal_per_kg','gbp_per_kg']
    for col in float_cols:
        items_df[col] = items_df[col].apply(lambda row: Decimal(str(row)))
    items_dict = items_df.to_dict(orient='records')
    return items_dict
    
def main():
    items_dict = load_csv_data()
    writer = DynamodbWriter(table_name='food_nutrition_data', region_name='eu-north-1')
    responses = []
    for item in items_dict:
        responses.append(writer.write_single_item(item)['ResponseMetadata']['HTTPStatusCode'])
    return responses

print(main())