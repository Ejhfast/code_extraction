# Changing color of background of tkinter window by using colorchooser in python 3 and tkinter
color = colorchooser.askcolor()
color_name = color[1]    #to pick up the color name in HTML notation, i.e. the 2nd element of the tuple returned by the colorchooser
root.configure(background=color_name)
