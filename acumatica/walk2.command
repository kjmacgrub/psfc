#!/usr/bin/env python

import os

downloads = ("/Users/km/Downloads/")

files_in_dir = []

# r=>root, d=>directories, f=>files
for r, d, f in os.walk(downloads):
   for item in f:
      if '.txt' in item:
         # files_in_dir.append(os.path.join(r, item))
         files_in_dir.append(os.path.join(item))

for item in files_in_dir:
   print(item)