# Dividing a string into a list of smaller strings of certain length
&gt;&gt;&gt; mystr = "0110100001100101011011000110110001101111"
&gt;&gt;&gt; [mystr[i:i+8] for i in range(0, len(mystr), 8)]
['01101000', '01100101', '01101100', '01101100', '01101111']
