import requests


class WeatherService:
    baseUrl = "https://api.openweathermap.org/data/2.5/forecast"     #q={city name},{country code}
    appId = "d31fc45cfdeb71ded94c4fbd185e5ed1"
    @classmethod
    def getForecast(cls, city, country):
        response = requests.get(cls.baseUrl, params=[
            ('appid', cls.appId)
            ('q',f'{city},{country}')   # found in the URL of what the variable is 'q' and what its expecting city and country
        ])
        data = response.json()
        return data

if __name__ == "__main__":
    print(WeatherService.getForecast('new york', 'us'))
