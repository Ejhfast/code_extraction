# How to formulate an XPATH expression for an attribute that contains a certain string?
//div[@class = 'd3-tip bar-chart n'
    and contains(normalize-space(@style), 'opacity:1')]
