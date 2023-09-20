import streamlit as st
from dynamodb_interface.db_utils.dynamodb_writer import DynamodbWriter
from utils.add_data_inputs import add_per_kg_information, add_label_information

st.title("Add an Ingredient to the Database")

st.markdown(
    """
Use this page to add to the ingredient database. Share your favourite 
ingredients with others and use them to create new recipes.
"""
)

st.subheader("Ingredient Stats Calculator")

st.subheader("Save Ingredient")

input_method = st.selectbox("Choose input method", options=["Label information", "Per kg information"])

if input_method == "Per kg information":
    food_item = add_per_kg_information()
    
elif input_method == "Label information":
    food_item = add_label_information()

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
