from db_utils.dynamodb_reader import DynamodbReader

reader = DynamodbReader(table_name='food_nutrition_data', region_name='eu-north-1')

print(reader.scan_item_names())