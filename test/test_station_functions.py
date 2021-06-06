import unittest
from unittest.mock import patch
import pandas as pd
import src.station_functions as sf

class TestStationFunctions(unittest.TestCase):
    def setUp(self):
        self.mock_df = pd.DataFrame({
            "station_id": [1,1,2,2,2,3], 
            "date": [2000.001, 2000.148, 2000.459, 2001.284, 2001.386, 2000.083], 
            "temperature_c": [-16, 5, 22, 8, 14, -22]})
        self.patch_df = patch('src.station_functions.get_data', return_value=self.mock_df)
        self.patched_df = self.patch_df.start()
    
    def tearDown(self):
        self.patch_df.stop()

    def test_get_lowest_temp(self):
        val = sf.get_station_with_lowest_temp()
        assert val[0] == 3
        assert val[1] == 2000.083
    
    def test_get_lowest_temp_altered(self):
        self.mock_df = self.mock_df.append({"station_id": 4, "date": 2002.183, "temperature_c": -31}, ignore_index=True)
        self.patch_df = patch('src.station_functions.get_data', return_value=self.mock_df)
        self.patched_df = self.patch_df.start()
        val = sf.get_station_with_lowest_temp()
        assert val[0] == 4
        assert val[1] == 2002.183

    def test_get_most_fluctuation(self):
        val = sf.get_station_with_most_fluctuation()
        assert val == 1
    
    def test_get_date_most_fluctuation(self):
        val = sf.get_station_fluctuation_for_date(2001.100, 2001.400)
        assert val == 2

    #TODO: Add two more test cases altering the fluctuation values with a different expected result to ensure functionality