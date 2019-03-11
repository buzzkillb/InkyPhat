#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json

from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.YELLOW)

from PIL import Image, ImageFont, ImageDraw

print("""Inky pHAT: Denarius displays blockchain information.
""")

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 16)

daddress = "DNRXXXXXXXXXXXXXXXXXXXXXXXXXZeeDTw"
url = "https://www.coinexplorer.net/api/v1/D/address/balance?address=%s" % daddress
response = urllib.urlopen(url)
data = json.loads(response.read())
dbalance = ("D Balance=" + data['result'][daddress] + '\n' + daddress)

# Load our backdrop image
img = Image.open("/home/pi/d-text-logo.png")
draw = ImageDraw.Draw(img)

draw.text((10, 60), dbalance, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
