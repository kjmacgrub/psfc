
import csv
import os
from pathlib import *
import glob
import re
from zipfile import ZipFile
import pandas as pd

# Store the downloads folder path for user's machine

folder = str(os.path.join(Path.home(), "Downloads/"))

# Collect all the zip files

zipfiles = [os.path.basename(file) for file in glob.glob(folder + "*.zip")]

# Select the files that have UNFI-like naming
# Strip the extension from the zip file and use that as a directory name
# Extract the orders into the new directory

for file in zipfiles:
    if re.search("C\d{5}_.*zip", str(file)):
        order_directory = file.rsplit( ".", 1 )[ 0 ] 
        ZipFile(folder + file).extractall(folder + order_directory)

# Collect all the order files

        txtfiles = []
        for file in glob.glob(folder + order_directory + '/' + "*.txt"):
            txtfiles.append(file)
        for each in txtfiles:
            df = pd.read_csv(each)
            print(df)
'''

from zipfile import ZipFile

order_file = None

with ZipFile('config.zip') as zip_archive:
  order_file = zip_archive.read('config/docker/docker-compose.yaml')

print(order_file)

'''
# orders = []
# for file in zipfiles:
#     orders = ZipFile(file).namelist()
#     print(orders)
'''
zipfiles = [os.path.basename(file) for file in glob.glob(folder + "*.zip")]
for file in zipfiles:
    if re.search("C\d{5}_.*zip", str(file)):
        print (zipfiles.index(file) + 1 ," ", file)







acumatica_file = folder + "unfi_acumatica_" + ".csv"
print ('\nAcumatica upload file was created: ' + acumatica_file)

with open(acumatica_file, "w") as file:
    data_out = csv.writer(file, dialect='excel')
    data_out.writerow(['Transaction Descr.', 'Quantity', 'Unit Cost'])
    for row in invoice_list:
        data_out.writerow(row)
'''