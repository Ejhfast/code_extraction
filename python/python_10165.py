# Inserting xml nodes in an existing xml document with python
valeurs = doc.getElementsByTagName("providers").item(0)
element = doc.createElement("provider")
valeurs.appendChild(element)
