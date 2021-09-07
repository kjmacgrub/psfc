from reportlab.platypus     import Table

def genBodyTable(width, height):

    widthList = [
        width * 20/100,
        width * 15/100,
        width * 15/100,
        width * 15/100,
        width * 15/100,
        width * 15/100,
    ]

    heightList = [
        height * 20/100,
        height * 10/100,
        height * 10/100,
        height * 10/100,
        height * 10/100,
        height * 10/100,
        height * 10/100,
        height * 10/100,
    ]

    res = Table([
        ['Reference #', 'Invoice Date', 'Due Date', 'Invoice #', 'Amount', 'Vouchered By'],
        ['b', 'c', 'd', 'e', 'f', 'g'],
        ['h', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
    ],
    widthList,
    heightList)

    res.setStyle([
        ('GRID', (0,0), (-1,-1), 1, 'gray'),
    ])
    return res