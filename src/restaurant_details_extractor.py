import pandas as pd

def get_restaurant_data(restaurant_data, country_codes):
    print("Extracting restaurant details...")

    restaurant_details_list = []

    # Assign country to codes
    country_code_dict = {}
    for _, row in country_codes.iterrows():
        country_code_dict[row['Country Code']] = row['Country']

    # Extract restaurant details
    for search in restaurant_data:
        for restaurant_info in search['restaurants']:
            indiv_restaurant = restaurant_info['restaurant']
            if indiv_restaurant['location']['country_id'] in country_code_dict:
                restaurant_data = get_individual_data(indiv_restaurant, country_code_dict)
                if restaurant_data:
                    restaurant_details_list.append(restaurant_data)

    # Convert restaurant details to DataFrame and save to CSV
    df = pd.DataFrame(restaurant_details_list)
    df.to_csv('./output/restaurant_details.csv', index=False)

    print("Extracted restaurant details.")

def get_individual_data(restaurant_info, country_code_dict):

    # Check if restaurant has had past events since Steven only wants
    # restaurants with past events
    if 'zomato_events' not in restaurant_info:
        return None
    
    restaurant_data = {
        'Restaurant ID': restaurant_info['R']['res_id'],
        'Restaurant Name': restaurant_info['name'],
        'Country': country_code_dict[restaurant_info['location']['country_id']],
        'City': restaurant_info['location']['city'],
        'User Rating Votes': restaurant_info['user_rating']['votes'],
        'User Aggregate Rating': float(restaurant_info['user_rating']['aggregate_rating']),
        'Cuisines': restaurant_info['cuisines'],
        'Event Data': restaurant_info['zomato_events']
    }

    return restaurant_data