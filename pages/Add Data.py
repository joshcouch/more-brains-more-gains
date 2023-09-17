import streamlit as st
from utils.food_item import FoodItem
from utils.constants import FOOD_ITEM, KCAL_PER_KG, GBP_PER_KG, G_PROTEIN_PER_KG
from dynamodb_interface.db_utils.dynamodb_writer import DynamodbWriter

st.title("Add an Ingredient to the Database")

st.markdown(
    """
Use this page to add to the ingredient database. Share your favourite 
ingredients with others and use them to create new recipes.
"""
)

st.subheader("Ingredient Stats Calculator")

st.subheader("Save Ingredient")

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

if food_item.check_valid_stats():
    
    # todo: add unique name validation

    writer = DynamodbWriter(table_name='food_nutrition_data', region_name='eu-north-1')

    if st.button("Save to database"):
        response = writer.write_single_item(food_item.to_dict())
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            st.write("Successfuly Saved Ingredient")
        
else:
    st.button(
        "Save to database",
        disabled=True,
        help="Fill out ingredient details to save"
    )
