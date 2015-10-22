# Finding and replacing XML/SVG element text by id with Python's lxml?
print tree.xpath("//n:text[@id='findme']/n:tspan/text()",
                 namespaces={'n': "http://www.w3.org/2000/svg"})
