from flask import Flask, request
import src.station_functions as sf

app = Flask(__name__)

@app.route('/lowest_station_temperature')
def get_lowest_temperature():
    val = sf.get_station_with_lowest_temp()
    return {'station_id': int(val[0]), 'date': float(val[1])}, 200

@app.route('/highest_station_fluctuation')
def get_fluctuation():
    date_args = request.args.get('dates')
    if date_args:
        dates = date_args.split(',')
        if len(dates) <= 1:
            return {'error': 'Invalid date parameters, must be in format: dates=val1,val2'}, 400
        val = sf.get_station_fluctuation_for_date(dates[0], dates[1])
    else:
        val = sf.get_station_with_most_fluctuation()
    return {'station_id': int(val)}, 200

if __name__ == '__main__':
    app.run()