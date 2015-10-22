# How to center frame in tkinter Canvas
x0 = self.frame.winfo_screenwidth()/2
y0 = self.frame.winfo_screenheight()/2
self.canvas.create_window((x0,y0), window=self.frame, anchor = "center")
