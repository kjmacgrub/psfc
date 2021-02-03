"""Step 2 in moving Clover invoice data to Acumatica.

Gather the files produced by acumat1.py, read into a dictionary, parse the filename, and calculate invoice totals.
"""
from decimal import *
import csv
import os
import pprint

getcontext().prec = 6
from pathlib import Path

invoices = []
data_folder = Path("/Users/ken_macdonald/Downloads/")
for (root, dirs, files) in os.walk(data_folder):
    for filename in files:
        if filename.endswith("txt"):
            filename_full = str(os.path.join(root, filename))
            with open(filename_full) as f:
                Total = 0
                reader = csv.DictReader(f)
                line_items = []
                for row in reader:
                    line_items.append(row)
                    Cost = Decimal(row["Unit Cost"])
                    Cases = Decimal(row["Quantity"])
                    Total += (Cases * Cost)
#                print(f'{filename:<70}{Total:,.2f}')
                invoices.append([filename] + [Total])
invoices.sort()
for x in invoices:
    print(str(x).replace("Decimal", ""))



