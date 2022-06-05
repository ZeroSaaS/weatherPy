#!/usr/bin/env python

import sys
import time
import math

#import weatherBit.py to call variables in that file
import weatherBit

# Import library and create instance of REST client.
from Adafruit_IO import Client

#use your client key from adafruit.io
aio = Client('YOUR_ADAFRUIT.IO_USERNAME', 'YOUR_ADAFRUIT.IO_KEY')

#try except to handle keyboard interrupt
try:
#while loop to continuously read data from analog input
    while True:
        #get temperature values from the temp variable in weatherBit.py and add value to the feed 'weatherbit'
        temp = weatherBit.temp
        aio.send_data('weatherbit.weatherbit', temp)

        #get weather description and add value to the feed 'description'
        desc = weatherBit.desc
        aio.send_data('weatherbit.description', desc)

        #get relative humidity and add value to the feed 'humidity'
        rh = weatherBit.rh
        aio.send_data('weatherbit.humidity', rh)

        #get 'aqi' air quality index from 'data' and add value to the feed 'aqi'
        aqi = weatherBit.aqi
        aio.send_data('weatherbit.aqi', aqi)
        
        #get 'pres' environmental pressure from 'data' and add value to the feed 'pres'
        pres = weatherBit.pres
        aio.send_data('weatherbit.pres', pres)

        #get 'sunset' sunset time from 'data' and add value to the feed 'sunset'
        sunset = weatherBit.sunset
        aio.send_data('weatherbit.sunset', sunset)

        #get 'sunrise' sunrise time from 'data' and add value to the feed 'sunrise'
        sunrise = weatherBit.sunrise
        aio.send_data('weatherbit.sunrise', sunrise)

        #get 'uv' uv index from 'data' and add value to the feed 'uv'
        uv = weatherBit.uv
        aio.send_data('weatherbit.uv', uv)

        #get 'precip' precipitation from 'data' and add value to the feed 'precip'
        precip = weatherBit.precip
        aio.send_data('weatherbit.precip', precip)

        #wait 5 minutes before cycling through the while loop again
        time.sleep(300)

except KeyboardInterrupt:
        pass
