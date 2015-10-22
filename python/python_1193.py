# python: xml.etree.ElementTree, removing "namespaces"
root.findall("/n:molpro/n:job",
             namespaces=dict(n="http://www.molpro.net/schema/molpro2006"))
