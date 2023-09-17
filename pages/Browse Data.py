import streamlit as st
from dynamodb_interface.db_utils.dynamodb_reader import DynamodbReader
from utils.data_wrangling.data_browser import DataBrowser

reader = DynamodbReader(table_name='food_nutrition_data', region_name='eu-north-1')
browser = DataBrowser()

@st.cache_data
def load_all_items():
    return reader.scan_all_items()

all_items = load_all_items()

browser.load_db_items(all_items)

browser.display_data()

if st.button("Reload Data"):
    st.cache_data.clear()