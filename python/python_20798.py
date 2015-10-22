# Prepend text to existing mail body
tmp = newMail.Body.split('&lt;body&gt;')
# split by a known HTML tag with only one occurrence then rejoin
newMail.Body = '&lt;body&gt;'.join([tmp[0],yourString + tmp[1]])
