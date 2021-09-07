import json

with open('orders.json') as json_file:
    data = json.load(json_file)
    for p in data['orders']:
        print(p['Vendor'])
        print(p['VoucherNumber'])
        print(p['Date'])
        print(p['Amount'])
        print(p['VendorRef'])