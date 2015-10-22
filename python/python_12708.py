# how to add maya outliner to tabLayout
myOut= cmds.outlinerPanel()
cmds.control(myOut, edit=True, parent="outlinerLayout")
