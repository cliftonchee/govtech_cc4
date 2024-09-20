import unittest
import pandas as pd

class TestNull(unittest.TestCase):

    def test_null(self):
        csv_file = '../output/apr_2019_restaurant_details.csv'
        df = pd.read_csv(csv_file, keep_default_na=False)
        null_values = df.isnull().values.any()
        
        self.assertFalse(null_values, "CSV contains null or empty values.")

if __name__ == '__main__':
    unittest.main()
