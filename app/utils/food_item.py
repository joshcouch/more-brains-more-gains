from decimal import Decimal
from utils.constants import FOOD_ITEM, G_PROTEIN_PER_KG, GBP_PER_KG, KCAL_PER_KG, DATA_SOURCE

class FoodItem():
    def __init__(self):
        pass
    
    def assign_stats(self, stats: dict, data_source: str):
        self.food_item = stats[FOOD_ITEM]
        self.g_protein_per_kg = Decimal(str(stats[G_PROTEIN_PER_KG]))
        self.kcal_per_kg = Decimal(str(stats[KCAL_PER_KG]))
        self.gbp_per_kg = Decimal(str(stats[GBP_PER_KG]))
        self.data_source = data_source
        
    def check_valid_stats(self):
        return bool(self.food_item) \
            and bool(self.g_protein_per_kg) \
                and bool(self.kcal_per_kg) \
                    and bool(self.gbp_per_kg) \
                        and bool(self.data_source)
    
    def __str__(self):
        return str(self.__dict__)
    
    def to_dict(self):
        return {
            FOOD_ITEM: self.food_item,
            G_PROTEIN_PER_KG: self.g_protein_per_kg,
            KCAL_PER_KG: self.kcal_per_kg,
            GBP_PER_KG: self.gbp_per_kg,
            DATA_SOURCE: self.data_source,
        }