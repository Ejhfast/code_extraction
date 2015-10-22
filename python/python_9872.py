# Python Replacing Strings with Dictionary values
s = "I can do waaaaaaaaaaaaay better :DDDD!!!! I am sooooooooo exicted about it :))) Good !!"
re.sub(r'(.)(\1{2,})',r'\1/LNG',s)
&gt;&gt; 'I can do wa/LNGy better :D/LNG!/LNG I am so/LNG exicted about it :)/LNG Good !!'
