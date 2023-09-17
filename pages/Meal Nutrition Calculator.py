import streamlit as st
import pandas as pd
from utils.database_interface import save_recipe
from utils.calculate_nutrition import calc_portion_nutrition

# Load the dataset
@st.cache_data  # Cache the dataset for improved performance
def load_data():
    data = pd.read_csv("../price_per_protein/data/food_stats_per_kg.csv")
    return data

data = load_data()

# Title and Sidebar
st.title("Meal Nutrition Calculator")

# Select multiple foods
selected_foods = st.multiselect("Select Ingredients", data["NAME"])

# Filter the data based on selected foods
recipe_data = data[data["NAME"].isin(selected_foods)].copy()
recipe_data["Grams"] = 0.0

left, _, right = st.columns((1, 0.1, 1))

with left:
    # Display the selected foods and their nutritional information
    disp_config = {key: None for key in recipe_data.columns}
    disp_config['NAME'] = 'Ingredient'
    disp_config['Grams'] = 'Grams'
    st.subheader("Selected Foods")
    recipe_data = st.data_editor(recipe_data, column_config=disp_config)

with right:
    # Input number of portions
    st.subheader("")
    n_portions = st.number_input("Number of Portions:", value=1, min_value=1)

# Calculate the total nutritional information
recipe_portion_dict = calc_portion_nutrition(recipe_data, n_portions)

# Display the total nutritional information
st.subheader("Nutritional Information Per Meal Portion")
if recipe_portion_dict['Total calories (kcal)']:
    st.write(f"Total calories: {recipe_portion_dict['Total calories (kcal)']:.0f}kcal")
    st.write(f"Total protein: {recipe_portion_dict['Total protein (g)']:.2f}g")
    st.write(f"Cost per portion: £{recipe_portion_dict['Cost per portion (£)']:.2f}")
    st.write(f"Cost per 100 grams of protein: £{recipe_portion_dict['Cost per 100 grams of protein (£/kg)']:.2f}/kg")
    st.write(f"Calories per gram of protein: {recipe_portion_dict['Calories per gram of protein (kcal/g)']:.2f}kcal/g")

if not recipe_portion_dict['Total calories (kcal)']:
    st.write("No nutritional information available yet.")
else:
    recipe_name = st.text_input("Recipe Name:")
    st.button(
        "Save Meal", 
        on_click=save_recipe,
        kwargs={'recipe_name': recipe_name, 'recipes_path': 'data/saved_recipes.csv', 'new_recipe_dict': recipe_portion_dict}
    )