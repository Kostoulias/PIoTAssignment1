from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
humid = sense.get_humidity()
sense.show_message('Temp: {0:0.1f} *c'.format(temp), scroll_speed=0.05)
sense.show_message('Humidity: {0:0.2f}%'.format(humid), scroll_speed=0.05)
sense.clear()