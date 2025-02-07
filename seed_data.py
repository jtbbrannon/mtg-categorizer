from category_class import CardCategories, CardCategory
import os, yaml

import pandas as pd

def get_card_categories(user_input):
    """
    Used for testing UI with some data
    Mocks AI call to speed things up 
    """
    seed_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seed_data.yaml')
    with open(seed_data_path, 'r') as file:
        seed_data = yaml.safe_load(file)
    # print(seed_data)
    cards = [CardCategory(**d) for d in seed_data]
    return CardCategories(cards=cards)