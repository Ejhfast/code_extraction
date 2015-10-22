# parsing out a second delimited data structure
for number in str(row.get('PhoneNumbers')).split('|'):
  file.write("\t\t\t\t&lt;PHONENUM&gt;"+number+"&lt;/PHONENUM&gt;\n")
