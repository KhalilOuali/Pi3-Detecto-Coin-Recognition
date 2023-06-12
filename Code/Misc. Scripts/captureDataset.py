# Start a preview window
# Take photo each time you press Enter in the terminal
# Quit when you enter 'q'

from picamera2 import Picamera2, Preview

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
capture_config = picam2.create_still_configuration()
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)
picam2.start()

i = 0
while (input("> Enter: Take Photo {}. q: Quit.\n".format(i)) != 'q'):
	picam2.switch_mode_and_capture_file(capture_config, "{}.jpg".format(i))
	i += 1
	picam2.switch_mode(preview_config)

picam2.close()
