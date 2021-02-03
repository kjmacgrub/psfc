import os
from pathlib import Path
import re
import zipfile

# add ability to read zipped files

home = str(Path.home())
downloads = (home + "/Downloads/")
ziplist = []

# gather the UNITED zip files
# r=>root, d=>directories, f=>files
for r, d, f in os.walk(downloads):
   for item in f:namelist
   	if re.search(("C.{5}_.{9}.zip"),str(item)):
            ziplist.append(os.path.join(item))

ziplist.sort()

# print the orders contained in each zip file
for item in ziplist:
    print("Orders in:",item)
    zf = zipfile.ZipFile(downloads + item, 'r')
    for order in zf.namelist():
        print(order)
        # print data from order

        data = zf.read(order)
        #for line in data:
        # print(data)


# calculate totals for each order

# create acumatica files for all orders on an invoice
