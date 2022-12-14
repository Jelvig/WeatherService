import time
from weatherService import WeatherService
import argparse

def within_time(item, start, end):
    return item['dt'] > start and item['dt'] < end   # make sure we are checking times that we want


def makeUmbrellaDecision(city, country) -> bool:
    current_time = time.time()
    end_time = current_time + 12*3600
    wx = WeatherService.getForecast(city, country)
    wx = [x for x in wx if within_time(x, current_time, end_time)]    # get forecast from current time frame
    rain_probability = [x['rain']['3h'] for x in wx if 'rain' in x]
    if len(rain_probability) > 0 and max(rain_probability) > 0.1:   #  rain probability
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decide if we need an umbrella.')   #  Make a CLI tool that can be used, with description
    parser.add_argument('--city', type=str, default='new york',
                        help='city to check')
    parser.add_argument('--country', type=str, default='us',
                        help='country to check')
    args = parser.parse_args()

    city=args.city
    country=args.country

    if(makeUmbrellaDecision(city, country)):
        city = 'seattle'
        country = 'us'
        print(f'You need an umbrella today in {city}, {country}')
    else:
        print(f'You do NOT need an umbrella today in {city}, {country}')
