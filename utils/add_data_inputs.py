import streamlit as st
from utils.food_item import FoodItem
from utils.constants import FOOD_ITEM, G_PROTEIN_PER_KG, KCAL_PER_KG, GBP_PER_KG

def add_per_kg_information():

    food_item_name = st.text_input("Name of Ingredient")

    g_protein_per_kg = st.number_input("Grams of protein per kilogram (g/kg)")

    kcal_per_kg = st.number_input("Calories per kilogram (kcal/kg)")

    gbp_per_kg = st.number_input("Cost per kilogram (£/kg)")

    food_item = FoodItem()

    food_item.assign_stats(
        {
            FOOD_ITEM: food_item_name,
            G_PROTEIN_PER_KG: g_protein_per_kg,
            KCAL_PER_KG: kcal_per_kg,
            GBP_PER_KG: gbp_per_kg,
        },
        data_source="webapp",
    )
    
    return food_item

def add_label_information():
    food_item_name = st.text_input("Name of Ingredient")
    
    portion_size = st.number_input("Portion size (g)", min_value=0.01)

    g_protein_per_portion = st.number_input("Grams of protein per portion (g)")

    kcal_per_portion = st.number_input("Calories per portion (kcal)")

    left, _, right = st.columns([0.2, 0.02, 0.2])
    
    with left:
        gbp_per_product = st.number_input("Cost of product (£)")
    
    with right:
        n_portions = st.number_input("Portions per product", min_value=1.0)

    food_item = FoodItem()
    
    gbp_per_portion = food_item.convert_cost_per_product_to_per_portion(gbp_per_product, n_portions)
    
    g_protein_per_kg = food_item.convert_value_per_portion_to_per_kg(g_protein_per_portion, portion_size)
    kcal_per_kg = food_item.convert_value_per_portion_to_per_kg(kcal_per_portion, portion_size)
    gbp_per_kg = food_item.convert_value_per_portion_to_per_kg(gbp_per_portion, portion_size)

    food_item.assign_stats(
        {
            FOOD_ITEM: food_item_name,
            G_PROTEIN_PER_KG: g_protein_per_kg,
            KCAL_PER_KG: kcal_per_kg,
            GBP_PER_KG: gbp_per_kg,
        },
        data_source="webapp",
    )
    
    return food_item