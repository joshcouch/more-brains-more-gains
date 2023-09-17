import pandas as pd

def calc_portion_nutrition(recipe_data: pd.DataFrame, n_portions: int):
    portion_calories = (recipe_data["KCAL_PER_KG"] * recipe_data["Grams"] / 1000).sum() / n_portions
    portion_proteins = (recipe_data["G_PROTEIN_PER_KG"] * recipe_data["Grams"] / 1000).sum() / n_portions
    portion_cost = (recipe_data["GBP_PER_KG"] * recipe_data["Grams"] / 1000).sum() / n_portions
    cost_per_100_g_protein = portion_cost / portion_proteins * 100
    kcal_per_100_g_protein = portion_calories / portion_proteins
    ingredients = [f"{ingredient}, {weight}g" for ingredient, weight in zip(recipe_data.NAME.values, recipe_data.Grams.values)]
    
    portion_dict = {
        'Total calories (kcal)': portion_calories,
        'Total protein (g)': portion_proteins,
        'Cost per portion (£)': portion_cost,
        'Cost per 100 grams of protein (£/kg)': cost_per_100_g_protein,
        'Calories per gram of protein (kcal/g)': kcal_per_100_g_protein,
        'Ingredients (g)': ingredients,
    }
    
    return portion_dict