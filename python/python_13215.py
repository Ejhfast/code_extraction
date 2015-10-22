# re.sub adding a newline in python
print re.sub('&lt;crew_member([^\&gt;]*)&gt;.*&lt;/crew_member&gt;\n', '', xml, flags=re.DOTALL)
