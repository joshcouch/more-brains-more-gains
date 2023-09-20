import streamlit as st
from dynamodb_interface.db_utils.dynamodb_reader import DynamodbReader
from utils.data_wrangling.data_browser import DataBrowser
from utils.data_browser_plots import plot_bar
from utils.constants import PARTITION_KEY, G_PROTEIN_PER_GBP, PARTITION_KEY_PRETTY, G_PROTEIN_PER_GBP_PRETTY, \
    G_PROTEIN_PER_KCAL, G_PROTEIN_PER_KCAL_PRETTY

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
    
top_protein_per_gbp = browser.get_top_10_by_col(G_PROTEIN_PER_GBP)

fig, ax = plot_bar(top_protein_per_gbp, G_PROTEIN_PER_GBP, PARTITION_KEY, PARTITION_KEY_PRETTY, G_PROTEIN_PER_GBP_PRETTY)

st.pyplot(fig)

top_protein_per_kcal = browser.get_top_10_by_col(G_PROTEIN_PER_KCAL)

fig, ax = plot_bar(top_protein_per_kcal, G_PROTEIN_PER_KCAL, PARTITION_KEY, PARTITION_KEY_PRETTY, G_PROTEIN_PER_KCAL_PRETTY)

st.pyplot(fig)