import forecastio
import config
import datetime

class ForecastWrapper(object):
    def __init__(self):
        self.api_key = config.API_KEY
        self.lat     = config.LAT
        self.lng     = config.LNG
        self.forecast = forecastio.load_forecast(self.api_key, self.lat, self.lng)

    def willItRain(self):
        minutely_data = self.forecast.minutely().data
        now = datetime.datetime.now()

        for minute in minutely_data:
            if minute.d['precipProbability'] > .5:
                then = datetime.datetime.fromtimestamp(minute.d['time'])
                rain_start = (then - now)
                minutes_from_now = rain_start.seconds / 60
                print 'The odds are good in {0} minute(s))'.format(minutes_from_now)
                print 'Dark Sky prediction {0}'.format(minute.d)
