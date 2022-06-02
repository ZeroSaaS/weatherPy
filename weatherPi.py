#import requests for HTTP GET request, import JSON to parse response
import requests
import json

#weatherbit API request for current weather in a particular zip code and save JSON to variable 'data'
#replace YOUR_ZIP_CODE with your 5 digit zip code. replace YOUR_WEATHERBIT_KEY with your key from weatherbit.io.  
URL = "https://api.weatherbit.io/v2.0/current?&postal_code=YOUR_ZIP_CODE&country=US&key=YOUR_WEATHERBIT_KEY"
data = []
r = requests.get(url = URL)
data = r.json()

#extract 'temp' in 'data' and convert to fahrenheit
temp = ((data['data'][0]['temp']) * (9/5)) + 32

#get icon image from weatherbit using URL
icon = str(data['data'][0]['weather']['icon'])
icon_URL = "https://www.weatherbit.io/static/img/icons/" + icon + ".png"

#print the temperature to the screen and the URL of the weather icon to verify it is working properly.
print(f"The temperature is: {temp} outside")
print(icon_URL)
