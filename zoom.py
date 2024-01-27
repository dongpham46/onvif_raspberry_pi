from ptz_control import ptzControl

ptz = ptzControl()


for i in range(100):
	ptz.zoom(0.5)

ptz.stop()