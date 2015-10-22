# Reducing the following lines of PhotoImage code to as few lines as possible
types = ('Blue', 'Polka', 'Red', 'Stripe', 'Yellow', 'Purple', 'Pink', 'Orange', 'Crazy', 'Plain')
for t in types:
    setattr(self, '%sEgg' % t, PhotoImage(file='assets/%segg.gif' % t.lower()))
