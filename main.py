import time
import datetime
from adafruit_ht16k33 import segments
import board
import busio

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

# clear display
display.fill(0)

x = 0

while True:

	display.print(str(round(x, 2)))

	x+=.1

	time.sleep(0.1)
