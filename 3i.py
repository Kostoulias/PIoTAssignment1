from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

#defining the colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
t = sense.get_temperature()
h = sense.get_humidity()

if t > 18 and t < 30:
    bg = green
else:
    bg = red

sense.show_message('Temp: {0:0.1f} *c'.format(t), scroll_speed=0.05, back_colour=bg)
sense.show_message('Humidity: {0:0.1f}%'.format(h), scroll_speed=0.05, back_colour=blue)
sense.clear()

