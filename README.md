# rain-alert
This is meant to be a simple wrapper around the Python forecast.io library. My main purpose was to set different led lights off based on the forecast. Will probably use RPi.GPIO for that. 

Anyways, if you somehow find yourself here and find this useful, you will want to do two things:

1. Run `pip install -r requirements.txt`, ideally after creating and sourcing a virtualenv
2. Create a config.py file with the following format:
```
API_KEY="jkjfakljaslkdj10929" # this in no way reflects an actual API key for forecast.io
LAT=45.1234
LNG=45.9876
```
