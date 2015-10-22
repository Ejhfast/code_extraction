# How to vertically align Paragraphs within a Table using Reportlab?
t=Table(data)
t.setStyle(TableStyle([('VALIGN',(-1,-1),(-1,-1),'MIDDLE')]))
