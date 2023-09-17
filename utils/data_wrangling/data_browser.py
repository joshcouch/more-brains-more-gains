import pandas as pd
import streamlit as st
from utils.constants import PARTITION_KEY, G_PROTEIN_PER_KG, KCAL_PER_KG, GBP_PER_KG, \
    PARTITION_KEY_PRETTY, G_PROTEIN_PER_KG_PRETTY, KCAL_PER_KG_PRETTY, GBP_PER_KG_PRETTY, \
        G_PROTEIN_PER_KCAL, G_PROTEIN_PER_GBP, G_PROTEIN_PER_KCAL_PRETTY, G_PROTEIN_PER_GBP_PRETTY

class DataBrowser():
    def __init__(self):
        self.dtypes = {
            PARTITION_KEY: str,
            G_PROTEIN_PER_KG: float,
            KCAL_PER_KG: float,
            GBP_PER_KG: float
        }
    
    def _item_list_to_df(self, item_list: list):
        self.df = pd.DataFrame(item_list)
    
    def _calculate_protein_densities(self):
        self.df[G_PROTEIN_PER_KCAL] = self.df[G_PROTEIN_PER_KG] / self.df[KCAL_PER_KG]
        self.df[G_PROTEIN_PER_GBP] = self.df[G_PROTEIN_PER_KG] / self.df[GBP_PER_KG]
    
    def load_db_items(self, db_items_list: list):
        self._item_list_to_df(db_items_list)
        self.df = self.df.astype(self.dtypes)
        self.df.set_index(PARTITION_KEY, drop=True)
        self._calculate_protein_densities()
        
    def display_data(self):
        pretty_col_names = {
            PARTITION_KEY: PARTITION_KEY_PRETTY,
            G_PROTEIN_PER_KG: G_PROTEIN_PER_KG_PRETTY,
            KCAL_PER_KG: KCAL_PER_KG_PRETTY,
            GBP_PER_KG: GBP_PER_KG_PRETTY,
            G_PROTEIN_PER_KCAL: G_PROTEIN_PER_KCAL_PRETTY,
            G_PROTEIN_PER_GBP: G_PROTEIN_PER_GBP_PRETTY,
        }
        self.clean_df = st.dataframe(
            self.df.copy(),
            column_order=pretty_col_names.keys(),
            column_config=pretty_col_names,
            hide_index=True
        )