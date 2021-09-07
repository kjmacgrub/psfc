import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,PageBreak
from reportlab.lib import colors
pdf=SimpleDocTemplate("vouchers.pdf")
flow_obj=[]

# import the json file and create column headers
with open('orders2.json') as json_file:
    data = json.load(json_file)
    orders = data["orders"]
    tabledata = []
    col1 = "Reference #"
    col2 = "Date"
    col3 = "Due date -- vendor"
    col4 = "Invoice"
    col5 = "Amount"
    col6 = "Vouchered By"
    rowdetail=[col1,col2,col3,col4,col5,col6]
    tabledata.append(rowdetail)

# for each line in the json file, append values in each column to the table 
    for line in range(len(orders)):
        rowdetail = []
        voucher_num = orders[line]["VoucherNumber"]["value"]
        reference = orders[line]["ReferenceNbr"]["value"]
        date = orders[line]["Date"]["value"]
        duedate = ""
        invoice = orders[line]["VendorRef"]["value"]
        amount = orders[line]["Amount"]["value"]
        vendor = orders[line]["Description"]["value"]
#        detail = orders[line]["Details"]
        voucheredby = ("KM")
        rowdetail.append(reference)
        rowdetail.append(date)
        rowdetail.append(vendor)
        rowdetail.append(invoice)
        rowdetail.append(amount)
        rowdetail.append(voucheredby)
        tabledata.append(rowdetail)
        print(rowdetail)

for i in range(len(tabledata)):
    if(i%10==0 and i>0): 
        flow_obj.append(PageBreak())      
        t=Table([tabledata[0]],colWidths=[50,50,50,100,30,50],repeatRows=1) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                       ("BACKGROUND",(0,0),(-1,-1),colors.white)]) # all except first page
    
        t.setStyle(tstyle)  
        flow_obj.append(t)              
    if (i==0):
        t =Table([tabledata[0]],colWidths=[50,50,50,100,30,50],repeatRows=2) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.gray),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                        ("BACKGROUND",(0,0),(-1,-1),colors.grey)]) # first page

        t.setStyle(tstyle)  
        flow_obj.append(t)
        
    else: 
        t=Table([tabledata[i]],colWidths=[50,50,50,100,30,50],repeatRows=1) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.gray),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5)])
                        
    
        t.setStyle(tstyle)  
        flow_obj.append(t)     
pdf.build(flow_obj)

