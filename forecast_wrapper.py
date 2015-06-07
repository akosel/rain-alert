import forecastio
import config

class ForecastWrapper(object):
    def __init__(self):
        self.api_key = config.API_KEY
        self.lat     = config.LAT
        self.lng     = config.LNG
        self.forecast = forecastio.load_forecast(self.api_key, self.lat, self.lng)

    def willItRain(self):
        minutely_data = self.forecast.minutely().data

        for minute in minutely_data:
            print minute.d
