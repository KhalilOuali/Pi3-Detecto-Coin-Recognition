# logging and audio output
from datetime import datetime
import time, logging
import subprocess 

logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.INFO)
now = datetime.now()
formatted_time = now.strftime('%A, %d %B %Y %H:%M:%S')
logging.info(f' Started {formatted_time}')
t = time.perf_counter()

def logTime(str):
	global t
	logging.info(f' {str} [{time.perf_counter() - t :.2f}s]')
	t = time.perf_counter()

def say(str):
	subprocess.run(f'espeak -v en -s 120 "{str}"', shell=True, check=True)

say('Program started. Please wait.')

# imports
import torch
from detecto import core
from picamera2 import Picamera2
import cv2
from gpiozero import Button
from signal import pause

logTime('Modules imported')

# model
inModel = torch.load('inModel.pth', map_location=torch.device('cpu'))
model = core.Model(['f', 's', 'y'])
model._model = inModel
logTime('Model loaded')

# camera
picam2 = Picamera2()
capture_config = picam2.create_still_configuration({"size": (800, 600)})
picam2.align_configuration(capture_config);
picam2.configure(capture_config)
picam2.start()
logTime('Camera started')

# detection function
def detect():
	global t
	t = time.perf_counter()
	print('> Taking photo...')
	image = picam2.capture_array()

	print('> Detecting...')
	say('Detecting. Please wait.')
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	predictions = model.predict(image)

	sum = 0
	logStr = 'Detected '
	for label, _, score in zip(*predictions):
		if score < 0.6:
			continue
		logStr += label

		if label == 'y':
			sum += 100
		elif label == 's':
			sum += 1000
		else:
			sum += 5000
	d, m = divmod(sum, 1000)

	print(f'➡️ {d} dinars and {m} millimes.')
	say(f'{d} dinars and {m} millimes.')
	
	logTime(logStr)
	print('✅ Ready.')
	say('Ready to detect.')
	
# button
button = Button(2)
button.when_pressed = detect

# ready
logTime('Ready')
print('✅ Ready.')
say('Ready to detect.')

while(True):
	pause()
