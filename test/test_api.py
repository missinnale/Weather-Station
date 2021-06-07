import pandas as pd
import unittest
from unittest.mock import patch

import src.api.api as api

class TestAPI(unittest.TestCase):

    def setUp(self) -> None:
        api.app.testing = True
        self.client = api.app.test_client()

        self.mock_df = pd.DataFrame({
            "station_id": [1,1,2,2,2,3], 
            "date": [2000.001, 2000.148, 2000.459, 2001.284, 2001.386, 2000.083], 
            "temperature_c": [-16, 5, 22, 8, 14, -22]})
        self.patch_df = patch('src.station_functions.get_data', return_value=self.mock_df)
        self.patched_df = self.patch_df.start()
    
    def tearDown(self):
        self.patch_df.stop()
    
    def test_lowest_temp(self):
        with self.client as c:
            res = c.get('/lowest_station_temperature')
            assert res.status_code == 200
            assert res.json['station_id'] == 3
            assert res.json['date'] == 2000.083
    
    def test_max_flucts(self):
        with self.client as c:
            res = c.get('/highest_station_fluctuation')
            assert res.status_code == 200
            assert res.json['station_id'] == 1
    
    def test_max_flucts_date_range(self):
        with self.client as c:
            date1 = 2001.100
            date2 = 2001.400
            res = c.get(f'/highest_station_fluctuation?dates={date1},{date2}')
            
            assert res.status_code == 200
            assert res.json['station_id'] == 2
    
    def test_max_flucts_date_range_input_error(self):
        with self.client as c:
            date1 = 2001.100
            date2 = 2001.400
            # using semicolon seperator to throw error
            res = c.get(f'/highest_station_fluctuation?dates={date1};{date2}')
            
            assert res.status_code == 400
            assert res.json['error'] == "Invalid date parameters, must be in format: dates=val1,val2"