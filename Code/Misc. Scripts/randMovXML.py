# Randomly move n xml files to a subdirectory

import os
import shutil
import random

n = 20
subdir = "val_labels/"
l = list(filter(lambda s: s.endswith(".xml"), os.listdir()))
for i in range(n):
		r = random.randint(0, len(l)-1)
		shutil.move(l[r], subdir + l[r])
		l.pop(r)
