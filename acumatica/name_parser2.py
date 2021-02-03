import os
from pathlib import Path
from decimal import *
import csv
getcontext().prec = 7
zip_folder = Path("/Users/km/Downloads/")

def get_voucher_number(name_stub):
    voucher_number = None
    assigned_voucher_numbers = {
        "Agrarian Feast": "29",
        "Alberts Organics": "30",
        "Baldor Specialty Foods": "31",
        "Blue Heron": "32",
        "Blue Moon Acres": "33",
        "Eli and Ali": "34",
        "Flora Nurseries": "35",
        "Four Seasons Produce": "36",
        "Fresh Meadow Organic": "37",
        "Gotham Greens": "38",
        "Grindstone": "39",
        "Hepworth Farms": "40",
        "Hudson Valley Harvest": "41",
        "Jeddas Produce": "42",
        "Lancaster Farm Fresh": "43",
        "Mushrooms NYC": "44",
        "Myers produce": "45",
        "Painters": "46",
        "Perfect Foods": "47",
        "RL Irwin": "48",
        "Regional Access": "49",
        "Rose Valley Farm": "50",
        "Square Roots": "51",
        "Sweet Melons": "52",
        "Wilklow Orchards": "53",
        "Element Farms": "54",
        "Wessels Farms": "55",
    }

    for assigned_supplier in assigned_voucher_numbers.keys():
        if name_stub in assigned_supplier.lower():
            voucher_number = assigned_voucher_numbers[assigned_supplier]
            break
    return str(voucher_number)

def get_supplier_ID(name_stub):
    ID_number = None
    assigned_ID_numbers = {
        "Agrarian Feast": "V100958",
        "Alberts Organics": "V100012",
        "Baldor Specialty Foods": "V100038",
        "Blue Heron": "V100060",
        "Blue Moon Acres": "V100671",
        "Eli and Ali": "V100774",
        "Flora Nurseries": "V100655",
        "Four Seasons Produce": "V100171",
        "Fresh Meadow Organic": "V100749",
        "Gotham Greens": "V100789",
        "Grindstone": "V100195",
        "Hepworth Farms": "V100201",
        "Hudson Valley Harvest": "V100775",
        "Jeddas Produce": "V100231",
        "Lancaster Farm Fresh": "V100245",
        "Mushrooms NYC": "V101095",
        "Myers produce": "V100928",
        "Painters": "V100334",
        "Perfect Foods": "V100351",
        "RL Irwin": "V100745",
        "Regional Access": "V100382",
        "Rose Valley Farm": "V100814",
        "Square Roots": "V101030",
        "Sweet Melons": "V101004",
        "Wilklow Orchards": "V101074",
        "Element Farms": "V101103",
        "Wessels Farms": "V101105",
    }

    for assigned_ID in assigned_ID_numbers.keys():
        if name_stub in assigned_ID.lower():
            ID_number = assigned_ID_numbers[assigned_ID]
            break
    return ID_number

d_inv = {}
for (root, dirs, files) in os.walk(zip_folder):
    for filename in files:
        if filename.endswith("csv"):
            
# Split the filename into parts
            
            filename_parts = filename.split("_")
            supplier = str(filename_parts[0]).replace("-", " ")
            invoice = filename_parts[1]
            invoice = invoice.upper()
            date = filename_parts[2]
            mth = date[-9:-7]
            day = date[-6:-4]
            yr = date[-12:-10]
            datestr = f'{mth}/{day}/{yr}'
            voucher_number = str('0' + get_voucher_number(supplier[:7]))
            supplier_ID = get_supplier_ID(supplier[:7])

# Calculate invoice totals

            filename_full = str(os.path.join(root, filename))
            with open(filename_full) as f:
                Total = 0
                reader = csv.DictReader(f)
                line_items = []
                for row in reader:
                    line_items.append(row)
                    Cost = Decimal(row["Unit Cost"])
                    Cases = Decimal(row["Quantity"])
                    Total += Decimal(Cases * Cost)

# Create dictionary with invoice totals
                key = str(filename_parts[0]) + invoice
                d_inv[key] = [supplier, supplier_ID, voucher_number, datestr, invoice, Total,]

# Sort and print the dictionary

d_inv_sort = {k: d_inv[k] for k in sorted(d_inv, reverse=True)}
for val in d_inv_sort.values():
    for item in val:
        print(item)
    print("---------------------")

# Create a csv file from the dictionary

with open('vouchers_sorted.csv', 'w') as f:
    for key in d_inv_sort.keys():
        f.write("%s,%s\n"%(key,d_inv_sort[key]))





