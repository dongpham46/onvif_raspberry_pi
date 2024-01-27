from ptz_control import ptzControl

ptz = ptzControl()

for i in range(200):
	ptz.move_pan(0.5)

ptz.stop()