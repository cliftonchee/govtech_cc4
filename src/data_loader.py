import pandas as pd
import json

def load_data():
    # Load restaurant data
    with open('data/restaurant_data.json', 'r') as file:
        restaurant_data = json.load(file)
    
    # Load country codes
    country_codes = pd.read_excel('data/Country-Code.xlsx')
    
    return restaurant_data, country_codes