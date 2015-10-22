# Error: Attribute error in TCL
sin_put=ttk.Entry(self.scanframe, width = 50)  ## stores the return ID from Entry
    sin_put.grid(row=0,column=1,padx=5,pady=10)  ## don't catch return from grid as it is None
