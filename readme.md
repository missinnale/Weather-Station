# Weather Station

### Overview
The original challenge is located inside `src.station_functions.py`. In there are located the three functions corresponding to the three parts of the challenge. The test cases for which are located in `test.test_station_functions.py`. ~~`Data.csv` could not be added to the github repo and was thus ignored, if you would like to run the functions with that data set, please download it seperately and add it to the file location `data/data.csv` so that it may be acquired in the functions correctly. As I am at the two hour mark, I could put in a reader to unzip the data file before it does the read so that the `data.csv` file could be included in the repo, but that would take additional time and I wanted to be fair with the work that I have done.~~ `Data.csv.zip` is now included in the repo and an unzip function has been added to accommodate so that the data can be read correctly. The calculate fluctuation function has now been converted to use `pandas` instead of a secondary dictionary to find the station with the maximum fluctuation. This has cut the runtime down by about 40min, since looping through 5million iterations takes a long time.

Additionally I have an api based around these functions in order to showcase my api abilities since the challenge was unrelated to such and that is where my abilities were questioned. You can find these in `src.api`. Here there will be a flask api laid out for showcasing any interactions with the previous challenge functions.

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
The api has a total of 2 endpoints, both are `GET` requests.

#### `/lowest_station_temperature`
This endpoint will retrieve the station and date of the lowest temperature in the `data.csv` file. With a response that looks like the following:
```json
{
    'station_id': station_value, # type -> int 
    'date': date_value # type -> float
}
```

#### `/highest_station_fluctuation`
This endpoint will retrieve the station id with the most fluctuation in total or based on provided date parameters. The request url should contain the following:
```
/highest_station_fluctuation?date=date1,date2
```
Where `date1` and `date2` is the inclusive range that you would like to check the fluctuation for.

Alternatively you may just use the request:
```
/highest_station_fluctuation
```
And it will check everything.

The response will look like the following:
```json
{
    'station_id': station_id # type -> int
}
```

## Additional Comments
The original commit contains the work done at the 2hr mark, most / about half of the work done there is research and understanding of the pandas library since I'm a bit unfamiliar but it seemed like the best way to accomplish the task at hand. I probably could have made some further advancements and efficiencies in the code using pandas instead of using additional data structures but I wanted to get something working within the 2 hrs. Thus the given fluctuation calculation that runs through 5million iterations is extremely slow (about 40min to run through the whole data set), however it does work. 

As expected though switching this function to use pandas to calculate the fluctuation is an extreme improvement over the manual work done as shown in the most recent commit, which takes a few seconds to run through the whole data set instead of the previous atrocious 40min.