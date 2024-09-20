import unittest
import pandas as pd

class TestApril2019Dates(unittest.TestCase):
    
    def test_all_dates_in_april_2019(self):
        csv_file = '../output/apr_2019_restaurant_details.csv'
        df = pd.read_csv(csv_file)
        
        years_start = df['Event Start Date'].str[:4]
        years_end = df['Event End Date'].str[:4]
        months_start = df['Event Start Date'].str[5:7]
        months_end = df['Event End Date'].str[5:7]
        
        in_april = (months_start == '04') | (months_end == '04')
        in_2019 = (years_start == '2019') | (years_end == '2019')

        self.assertTrue((in_april & in_2019).all(), "Not all events are in April 2019")

if __name__ == '__main__':
    unittest.main()
