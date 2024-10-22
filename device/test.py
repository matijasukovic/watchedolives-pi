from picamera2 import Picamera2, Preview
from libcamera import controls

from gpiozero import OutputDevice

from pynput import keyboard


# Laser head setup

from classes.laser_head import LaserHead

head = LaserHead()

# Laser setup

laser = OutputDevice(17)

# Camera setup

from classes.camera import Camera

camera = Camera()

def on_press(key):
	if key == keyboard.Key.esc:
		laser.off()
		head.pan.mid()
		head.tilt.mid()
		return False  # stop listener

	try:
		k = key.char  # single-char keys
	except:
		k = key.name  # other keys

	if k in ['left', 'right', 'up', 'down', 'enter', '0']:  # keys of interest
		controlDevice(k)
	elif k in ['space']:
		camera.captureAndSave()


def controlDevice(button):
	increment = 0.5

	if button == "up" and head.tilt.getAngle() + increment < 180:
		head.setTiltAngle(head.tilt.getAngle() + increment)
		print('tilt up', head.tilt.getAngle())
	elif button == "down" and head.tilt.getAngle() - increment > 0:
		head.setTiltAngle(head.tilt.getAngle() - increment)
		print('tilt down ', head.tilt.getAngle())
	elif button == "left" and head.pan.getAngle() + increment < 180:
		head.setPanAngle(head.pan.getAngle() + increment)
		print('pan left ', head.pan.getAngle())
	elif button == "right" and head.pan.getAngle() - increment > 0:
		head.setPanAngle(head.pan.getAngle() - increment)
		print('pan right ', head.pan.getAngle())
	elif button == "enter":
		laser.toggle()
	elif button == '0':
		laser.off()
		head.pan.mid()
		head.tilt.mid()


def main():
	head.pan.mid()
	head.tilt.mid()

	camera.startPreview()

	listener = keyboard.Listener(on_press=on_press)
	listener.start()  # start to listen on a separate thread
	listener.join()  # remove if main thread is polling self.keys   
	
if __name__ == '__main__':
	main()