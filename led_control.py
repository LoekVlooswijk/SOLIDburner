import time
from rpi_ws281x import *
import argparse

LED_COUNT = 30
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 65
LED_INVERT = False
LED_CHANNEL = 0


def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000)


def wheel(pos):
	if pos < 85:
		return Color(pos*3, 255-pos*3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 -pos*3, 0, pos*3)
	else:
		pos -= 170
		return Color(0, pos*3, 255-pos*3)


def rainbowCycle(strip, wait_ms=20, iterations=5):
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i*256/strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000)




if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
	args = parser.parse_args()
	
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	
	if not args.clear:
		print('use -c argument to clear leds on exit')
	
	try:
		
		while True:
			rainbowCycle(strip)
			
	except KeyboardInterrupt:
		if args.clear:
			colorWipe(strip, Color(0,0,0), 10)
