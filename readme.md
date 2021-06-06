# Weather Station

### Overview
The original challenge is located inside `src.station_functions.py`. In there are located the three functions corresponding to the three parts of the challenge. The test cases for which are located in `test.test_station_functions.py`.

Additionally I am adding an api based around these functions in ordre to showcase my api abilities since the challenge was unrelated to such and that is where my abilities were questioned. You can find these in `src.api`. Here there will be a flask api laid out for showcasing any interactions with the previous challenged functions.

### Installation
To install all the requirements to run please set up your virtual environment. My personal preference is to use virtualenvwrapper, which you can download with:
```bash
$ pip install virtualenvwrapper
```

To create an environment you would execute the following:
```bash
$ mkvirtualenv weather_station
```

To install the requirements in your virtual environment execute the following:
```bash
(weather_station)$ pip install -r requirements.txt
```

### Running tests
Tests may be run from the top level directory (and is preferable since references are made from here) since the project has been made into a package.
Execute the following in order to run all the tests:
```bash
(weather_station)$ python -m unittest
```

### API
`To Be added once api is complete`