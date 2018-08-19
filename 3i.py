#!/usr/bin/env python3
import os
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

h = sense.get_humidity()
t = sense.get_temperature()
t_corr = t - 21 

sense.show_message('Temp: {0:0.1f}*c'.format(t_corr), scroll_speed=0.05)
sense.show_message('Humidity: {0:0.1f}%'.format(h), scroll_speed=0.05)
sense.clear()
