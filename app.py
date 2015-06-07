import forecastio
import config

api_key = config.API_KEY
lat = 42.3076
lng = -83.7398

forecast = forecastio.load_forecast(api_key, lat, lng)
print forecast.hourly()
