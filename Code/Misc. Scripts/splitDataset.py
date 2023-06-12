# Randomly split images in current directory 
# into subdirectories a, b, c, ... with 17 images each.

import os
import shutil
import random

l = list(filter(lambda s: s.endswith(".jpg"), os.listdir()))
newDir = 'a'
while len(l) > 0:
    print(newDir)
    os.mkdir(newDir)
    for i in range(17):
        r = random.randint(0, len(l)-1)
        shutil.move(l[r], newDir + "/" + l[r])
        l.pop(r)
        if (len(l) <= 0):
            break
    newDir = chr(ord(newDir)+1)
