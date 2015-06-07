import forecastio
import config

api_key = config.API_KEY
lat = config.LAT 
lng = config.LNG

forecast = forecastio.load_forecast(api_key, lat, lng)
print forecast.hourly()
