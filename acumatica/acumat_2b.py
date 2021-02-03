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
        if filename.endswith("csv"):

            filename_parts = filename.split('_')
            supplier = str(filename_parts[0]).replace("-", " ")
            invoice = filename_parts[1]
            invoice = invoice.upper()
            date = filename_parts[2]
            mth = date[-9:-7]
            day = date[-6:-4]
            yr = date[-12:-10]

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
                invoices.append([supplier] + [invoice] + [mth] + [day] + [yr] + [Total] + [date])
invoices.sort()

for x in invoices:
    print(f'{x}'.replace("Decimal", ""))
    print(str(x).replace("Decimal", ""))



