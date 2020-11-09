import time
import datetime
from adafruit_ht16k33 import segments
import board
import busio
import obd
import re

#setup connection to bt obd crap
obd.logger.setLevel(obd.logging.DEBUG)
ports = obd.scan_serial()
if len(ports) == 0:
	time.sleep(1)
	raise Exception("no bt things!")
#guess we found a serial thing now

#open it up for real
connection = obd.OBD(ports[0])



# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

# clear display
display.fill(0)


while True:
	val = connection.query(obd.commands["SPEED"]).value
	print(val)
	out = re.findall("\d+\.\d+", str(val))

	if len(out) == 0:
		display.print(str(" 0ff")[::-1])
		time.sleep(.2)
		continue

	display.print("0000" + str(float(str(out[0]))*0.621371)[::-1])

#	print(round(x,0))
#	print(x)
#	x+=1


	time.sleep(0.1)
#	input("enter for next")
