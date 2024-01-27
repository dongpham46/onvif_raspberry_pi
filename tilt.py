from ptz_control import ptzControl

ptz = ptzControl()

for i in range(200):
	ptz.move_tilt(-0.9)

ptz.stop()
