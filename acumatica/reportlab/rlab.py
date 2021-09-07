from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,PageBreak
from reportlab.lib import colors
import csv
pdf=SimpleDocTemplate("vouchers.pdf")
flow_obj=[]
with open("vouchertotals.csv", encoding='ISO-8859-1') as f1:
    csvdata=csv.reader(f1,delimiter=",")
    tdata=[]
    for data in csvdata:
        rowdata=[]
        voucher=data[1]
        reference=data[2]
        date=data[3]
        due=data[4]
        invoice=data[5]
        amount=data[6]
        vendor=data[7]
        rowdata.append(voucher)
        rowdata.append(reference)
        rowdata.append(date)
        rowdata.append(due)
        rowdata.append(invoice)
        rowdata.append(amount)
        rowdata.append(vendor)
        tdata.append(rowdata)        
    tdata.sort
for i in range(len(tdata)):
    if(i%30==0 and i>0): 
        flow_obj.append(PageBreak())      
        t=Table([tdata[0]],colWidths=[50,50,50,50,100,50]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                       ("BACKGROUND",(0,0),(-1,-1),colors.greenyellow)]) # all except first page
    
        t.setStyle(tstyle)  
        flow_obj.append(t)              
    if (i==0):
        t =Table([tdata[0]],colWidths=[50,50,50,100,50]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.gray),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                        ("BACKGROUND",(0,0),(-1,-1),colors.gray)]) # first page

        t.setStyle(tstyle)  
        flow_obj.append(t)
        
    else: 
        t=Table([tdata[i]],colWidths=[50,50,50,50,100,50]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.gray),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5)])
                        
    
        t.setStyle(tstyle)  
        flow_obj.append(t)     
pdf.build(flow_obj)