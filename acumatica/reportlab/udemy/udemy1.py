from reportlab.lib import pagesizes
from reportlab.pdfgen   import canvas
from reportlab.lib.pagesizes    import LEGAL, LETTER
from reportlab.platypus     import Table    
from header import genHeaderTable
from body import genBodyTable
from footer import genFooterTable

pdf = canvas.Canvas('report.pdf', pagesize=LETTER)
pdf.setTitle('Udemy class')

width, height = LETTER
heightList = [
    height * 35/100,
    height * 55/100,
    height * 10/100,
]

mainTable = Table([
    [genHeaderTable(width,heightList[0])],
    [genBodyTable(width,heightList[1])],
    [genFooterTable(width,heightList[2])],
],
colWidths=width,
rowHeights= heightList
)

mainTable.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'gray'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0,),

])

mainTable.wrapOn(pdf, 0, 0)
mainTable.drawOn(pdf,0,0)


pdf.showPage()
pdf.save()