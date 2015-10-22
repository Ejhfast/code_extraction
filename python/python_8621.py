# Python Tkinter text background
i=w.create_text(*textSet, text=i[3], font=("Helvetica", 16))
r=w.create_rectangle(w.bbox(i),fill="white")
w.tag_lower(r,i)
