import pandas as pd

def get_apr_2019_restaurant_data(restaurant_data):
    print("Extracting restaurant details (Apr 2019)...")

    restaurant_details_list = []

    # Extract restaurant details
    for search in restaurant_data:
        for restaurant_info in search['restaurants']:
            indiv_restaurant = restaurant_info['restaurant']
            info = get_individual_info(indiv_restaurant)
            if info:
                restaurant_details_list.extend(info)

    # Convert restaurant details to DataFrame and save to CSV
    df = pd.DataFrame(restaurant_details_list)
    df.to_csv('./output/apr_2019_restaurant_details.csv', index=False)

    print("Extracted restaurant details (Apr 2019).")

def get_individual_info(restaurant_info):

    # Check if restaurant has had past events since Steven only wants
    # restaurants with past events
    if 'zomato_events' not in restaurant_info:
        return 
    
    event_list = []
    
    for event in restaurant_info['zomato_events']:

        event_data = event['event']
    
        # Check validity of month
        start_date = event_data['start_date']
        end_date = event_data['end_date']
        if not isInApril2019(start_date) and not isInApril2019(end_date):
            continue

        # Fill no photos (missing values) with NA
        photo_urls = 'NA'
        for photo in event_data['photos']:
            if photo_urls == 'NA':
                photo_urls = photo['photo']['url']
            else:
                photo_urls += photo['photo']['url']

        restaurant_data = {
            'Event ID': event_data['event_id'],
            'Restaurant ID': restaurant_info['R']['res_id'],
            'Restaurant Name': restaurant_info['name'],
            'Photo URL': photo_urls,
            'Event Title': event_data['title'],
            'Event Start Date': start_date,
            'Event End Date': end_date,
        }
        event_list.append(restaurant_data)

    return event_list

def isInApril2019(date):
    month = date[5:7]
    year = date[:4]
    return month == '04' and year == '2019'