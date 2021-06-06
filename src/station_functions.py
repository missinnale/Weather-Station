import pandas as pd

def get_data():
    data = pd.read_csv("../data/data.csv")
    return data

def get_fluctuation(data):
    stations = {}
    for i, val in enumerate(data["temperature_c"][1:], 1):
        if data["station_id"][i-1] == data["station_id"][i]:
            if data["station_id"][i] in stations:
                stations[data["station_id"][i]] += abs(data["temperature_c"][i-1] - val)
            else:
                stations[data["station_id"][i]] = abs(data["temperature_c"][i-1] - val)
            continue
        continue
    return stations

def get_station_with_lowest_temp():
    data = get_data()
    min_values = data.idxmin()
    return [data["station_id"][min_values[2]], data["date"][min_values[2]]]

def get_station_with_most_fluctuation():
    data = get_data()
    stations = get_fluctuation(data)
    max_station = max(stations, key= stations.get)
    return max_station

def get_station_fluctuation_for_date(date_1, date_2):
    response = get_data()
    data = response[(response["date"] >= date_1) & (response["date"] <= date_2)].reset_index()
    stations = get_fluctuation(data)
    max_station = max(stations, key= stations.get)
    return max_station