import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def determine_rating_thresholds(restaurant_data):

    print("Extracting rating thresholds...")

    ratings_list = []
    ratings = ["Poor", "Average", "Good", "Very Good", "Excellent"]

    # Extract restaurant details
    for search in restaurant_data:
        for restaurant_info in search['restaurants']:
            indiv_restaurant = restaurant_info['restaurant']
            ratings_list.append(float(indiv_restaurant['user_rating']['aggregate_rating']))

    print(ratings_list)
    ratings_list = np.array(ratings_list).reshape(-1, 1)

    # Apply k-means clustering to determine rating thresholds
    kmeans = KMeans(n_clusters=len(ratings), random_state=42).fit(ratings_list)
    thresholds = np.sort(kmeans.cluster_centers_.flatten())

    # Save thresholds to CSV
    df = pd.DataFrame({'Thresholds': thresholds, 'Ratings': ratings})
    df.to_csv('./output/rating_thresholds.csv', index=False)
   
    print("Extracted rating thresholds")