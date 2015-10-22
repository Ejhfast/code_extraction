# Tkinter GUI, Open File .. Button and BMP images .. Error on showing a selected file
pil_image = Image.open(tkFileDialog.askopenfilename())
image1 = ImageTk.PhotoImage(pil_image)
