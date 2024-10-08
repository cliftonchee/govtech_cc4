from src.data_loader import load_data
from src.restaurant_details_extractor import get_restaurant_data
from src.restaurant_details_apr_2019_extractor import get_apr_2019_restaurant_data
from src.determine_rating_thresholds import determine_rating_thresholds

def main():
    restaurant_data, country_codes = load_data()
    get_restaurant_data(restaurant_data, country_codes)
    get_apr_2019_restaurant_data(restaurant_data)
    determine_rating_thresholds(restaurant_data)

if __name__ == "__main__":
    main()

