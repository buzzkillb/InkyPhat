#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json

from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.YELLOW)

from PIL import Image, ImageFont, ImageDraw

print("""Inky pHAT: Bitcoin Price information.
""")

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 24)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
chartname = data['chartName']
btcusd = data['bpi']['USD']['rate_float']
btceur = data['bpi']['EUR']['rate_float']
bitcoinprice = (chartname + '\n' + "$ " + str(btcusd) + '\n' + "E " + str(btceur))

# Load our sprite sheet and prepare a mask
#text = Image.open("/home/pi/btc_yellow.png")
#text_mask = create_mask(text, [inky_display.WHITE])

# Load our backdrop image
img = Image.open("/home/pi/btc_yellow.png")
draw = ImageDraw.Draw(img)

#img = Image.open("/home/pi/btc_yellow.png")
draw.text((10, 10), bitcoinprice, inky_display.YELLOW, font)
inky_display.set_image(img)
inky_display.show()
