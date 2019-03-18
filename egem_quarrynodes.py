#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json

from inky import InkyPHAT

inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

print("""Inky pHAT: Denarius displays blockchain information.
""")

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

#font = ImageFont.truetype("/home/pi/fonts/OpenSans-SemiBold.ttf", 20)
font = ImageFont.truetype(FredokaOne, 19)

url = "https://api.egem.io/api/v1/nodes"
response = urllib.urlopen(url)
data = json.loads(response.read())
totalnodes = str(data['settings'][0]['data']['totalNodes'])
nodes1 = str(data['settings'][0]['data']['nodesOnline'])
nodes2 = str(data['settings'][0]['data']['nodesOnline2'])

nodestats = ("QuarryNodes: " + totalnodes + '\n' + "Q1: " + nodes1 + " Q2: " + nodes2)

# Load our backdrop image
img = Image.open("/home/pi/inky_egem_black.png")
draw = ImageDraw.Draw(img)

#w, h = font.getsize(winstats)
#x = (inky_display.WIDTH / 2) - (w / 2)
#y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((5, 55), nodestats, inky_display.BLACK, font)
flipped = img.rotate(180)
inky_display.set_image(flipped)
inky_display.show()
