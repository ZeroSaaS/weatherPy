#import requests for HTTP GET request, import JSON to parse response
import requests
import json

#weatherbit API request for current weather in a particular zip code and save JSON to variable 'data'
URL = "https://api.weatherbit.io/v2.0/current?&postal_code=YOUR_ZIP_CODE&country=US&key=YOUR_WEATHERBIT_KEY"
data = []
r = requests.get(url = URL)
data = r.json()

#extract 'temp' in 'data' and convert to fahrenheit
temp = round(((data['data'][0]['temp']) * (9/5)) + 32, 0)
#extract weather 'description' in data
desc = ""
desc = data['data'][0]['weather']['description']

#extract 'rh' relative humidity % in 'data'
rh = data['data'][0]['rh']

#extract 'aqi' air quality index from 'data'
aqi = data['data'][0]['aqi']

#extract 'pres' barometric pressure from 'data'
pres = data['data'][0]['pres']

#extract 'sunset' sunset time from 'data'
sunset = data['data'][0]['sunset']

#extract 'sunrise' sunrise time from 'data'
sunrise = data['data'][0]['sunrise']

#extract 'uv' uv index from 'data'
uv = data['data'][0]['uv']

#extract 'precip' precipitation from 'data'
precip = data['data'][0]['precip']
