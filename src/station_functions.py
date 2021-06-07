import pandas as pd
import numpy as np
import zipfile

def get_data():
    with zipfile.ZipFile("./data/data.csv.zip", 'r') as zip_ref:
        zip_ref.extractall("./data")
    data = pd.read_csv("./data/data.csv")
    return data

def get_fluctuation(data):
    stations = data.groupby("station_id")["temperature_c"].apply(np.diff).apply(np.abs).apply(np.sum)
    return stations.idxmax()

def get_station_with_lowest_temp():
    data = get_data()
    min_values = data.idxmin()
    return [data["station_id"][min_values[2]], data["date"][min_values[2]]]

def get_station_with_most_fluctuation():
    data = get_data()
    return get_fluctuation(data)

def get_station_fluctuation_for_date(date_1, date_2):
    response = get_data()
    data = response[(response["date"] >= float(date_1)) & (response["date"] <= float(date_2))].reset_index()
    return get_fluctuation(data)