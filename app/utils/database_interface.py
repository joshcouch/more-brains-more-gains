import pandas as pd

def save_recipe(recipe_name, recipes_path: str, new_recipe_dict):
    current_recipes = pd.read_csv(recipes_path)
    new_recipe_dict['Recipe Name'] = recipe_name
    new_recipe = pd.DataFrame(new_recipe_dict, index=[0])
    updated_recipes = pd.concat([current_recipes, new_recipe], axis=0)
    updated_recipes.to_csv(recipes_path, index=False)