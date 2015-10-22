# Remove grey borders from ttk.Button
ttk.Style().configure("RB.TButton", background='black')
ttk_btn = ttk.Button(text="ttk_Sample", style="RB.TButton")
