# Is there a way to encode unicode into a human readable variant of base64 (in python)
urllib.quote("'N@sty!!`` string,!!))'",safe=" ,.").replace('%','=')
'=27N=40sty=21=21=60=60 string,=21=21=29=29=27'
