from reportlab.platypus     import Table, Image

def genHeaderTable(width, height):


    ImgPath = 'VoucherHeader.png'
    ImgWidth = width
    Img = Image(ImgPath, ImgWidth, height)


    result = Table([[Img]], width, height)
    result.setStyle([
        ('GRID', (0,0), (-1,-1), 1, 'red'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0,),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),   
    ])
    return result