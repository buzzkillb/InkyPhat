#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json

from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.YELLOW)

from PIL import Image, ImageFont, ImageDraw

print("""Inky pHAT: Denarius Price information.
""")

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 22)

url = "https://api.coinpaprika.com/v1/coins/d-denarius/ohlcv/latest"
response = urllib.urlopen(url)
data = json.loads(response.read())
dhigh = data[0]['high']
dlow = data[0]['low']
dvol = data[0]['volume']
dmc = data[0]['market_cap']
denariusprice = ("$ " + str(dhigh) + '\n' + "$ " + str(dlow) + '\n' + "$ " + str(dvol) + '\n' + "$ " + '\n' + str(dmc))

# Load our backdrop image
img = Image.open("/home/pi/d-logo.png")
draw = ImageDraw.Draw(img)

#img = Image.open("/home/pi/btc_yellow.png")
draw.text((10, 0), denariusprice, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
