# Extract first paragraph using regex
#data - stuff between text tags
 firstparagraph = re.search("}}(.*?)\r*\n\r*\n",data,re.DOTALL)
 print firstparagraph.group(1)
