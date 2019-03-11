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

font = ImageFont.truetype(FredokaOne, 18)

daddress = "DSSziJxk6bvz5aX3LyCTQoiHGkXi8RA1bV"
url = "https://www.coinexplorer.net/api/v1/D/masternode?address=%s" % daddress

response = urllib.urlopen(url)
data = json.loads(response.read())

urlbalance = "https://www.coinexplorer.net/api/v1/D/address/balance?address=%s" % daddress

responsebalance = urllib.urlopen(urlbalance)
databalance = json.loads(responsebalance.read())

fs_status = (data['result'][0]['pubkey'] + '\n' + data['result'][0]['status'] + '\n' + data['result'][0]['ip'] + '\n' + databalance['result'][daddress] + "D")

# Load our backdrop image
img = Image.open("/home/pi/fs-logo.png")
draw = ImageDraw.Draw(img)

draw.text((10, 5), fs_status, inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show()
