# import boto3
import streamlit as st
from utils.constants import PARTITION_KEY, G_PROTEIN_PER_KG, KCAL_PER_KG, GBP_PER_KG

# class DynamodbReader():
#     def __init__(self, table_name: str, region_name: str ='eu-north-1'):
#         self.service_name = 'dynamodb'
#         self.table_name = table_name
#         self.region_name = region_name
#         aws_access_key_id = st.secrets['AWS_ACCESS_KEY_ID']
#         aws_secret_access_key = st.secrets['AWS_SECRET_ACCESS_KEY']
#         self.dynamodb = boto3.resource(
#             self.service_name,
#             region_name=self.region_name,
#             aws_access_key_id=aws_access_key_id,
#             aws_secret_access_key=aws_secret_access_key
#         )
#         self.table = self.dynamodb.Table(self.table_name)
        
#     def scan_db(self, attrs: list):
#         response = self.table.scan(AttributesToGet=attrs)
#         return response
    
#     def scan_item_names(self):
#         response = self.scan_db(attrs=[PARTITION_KEY])
#         item_names_list = [item[PARTITION_KEY] for item in response['Items']]
#         return item_names_list
    
#     def scan_all_items(self):
#         response = self.scan_db(
#             attrs=[PARTITION_KEY, G_PROTEIN_PER_KG, KCAL_PER_KG, GBP_PER_KG]
#         )
#         items = response['Items']
#         return items


from pathlib import Path
import pandas as pd


class CsvReader:
    def __init__(self, csv_path: str | Path = "data/initial_food_stats_per_kg.csv"):
        self.csv_path = Path(csv_path)
        self.df = pd.read_csv(self.csv_path)

    def reload(self) -> None:
        """Reload the CSV from disk if the file changes."""
        self.df = pd.read_csv(self.csv_path)

    def scan_db(self, attrs: list[str]) -> list[dict]:
        missing = [col for col in attrs if col not in self.df.columns]
        if missing:
            raise KeyError(f"Missing columns in {self.csv_path}: {missing}")
        return self.df[attrs].to_dict(orient="records")

    def scan_item_names(self) -> list[str]:
        if PARTITION_KEY not in self.df.columns:
            raise KeyError(f"Missing '{PARTITION_KEY}' column in {self.csv_path}")
        return self.df[PARTITION_KEY].dropna().tolist()

    def scan_all_items(self) -> list[dict]:
        cols = [PARTITION_KEY, G_PROTEIN_PER_KG, KCAL_PER_KG, GBP_PER_KG]
        return self.scan_db(attrs=cols)