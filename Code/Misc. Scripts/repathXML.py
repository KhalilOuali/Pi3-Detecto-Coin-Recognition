# Fix the path or name of the image file in the xml file
# Using regex replace

import os
import re

parent_dir = os.path.dirname(os.path.realpath(__file__))

for f in os.listdir(parent_dir):
	file_path = os.path.join(parent_dir, f)
	
	if not (os.path.isfile(file_path) and file_path.endswith(".xml")):
		continue
	
	with open(file_path, 'r') as file:
		contents = file.read()
	
	updated_contents = re.sub(r'(?<=(<filename>)).*(?=(</filename>))', f.replace('xml', 'jpg'), contents)
	
	with open(file_path, 'w') as file:
		file.write(updated_contents)
