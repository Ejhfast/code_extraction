# How to create gtk.STOCK_* buttons from a modified list of strings?
for button in stock_button_list:
    self.button1=gtk.Button(stock=getattr(gtk,button))
