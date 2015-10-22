# Using Reportlab Canvas- How to create an Option to print the pdf generated from the browser itself?
from reportlab.pdfbase import pdfdoc
pdfdoc.PDFCatalog.OpenAction = '&lt;&lt;/S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)&gt;&gt;'
