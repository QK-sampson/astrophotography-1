"""
	This module captures a series of images with different exposure settings
"""

from time import sleep
from picamera import PiCamera

#Initiation of camera
camera = PiCamera(framerate = 0.01)
camera.vflip = True
camera.hflip = True
camera.resolution = (1280,720)

camera.iso = 800

print("Waiting for 30 s")
#wait for a long time for the camera gain control to settle on a high value
sleep(30)

if __name__ == '__main__':
	try:
		for i in range(1,6):
			shutter_speed = i * 2000000
			camera.shutter_speed = shutter_speed
			print("capturing image with shutter_speed {}".format(shutter_speed))
			camera.capture("./images/s%d.jpg" % ( i * 2) );
			print("capture complete")
	finally:
		print("closing camera")
		camera.close()