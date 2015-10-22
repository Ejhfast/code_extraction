# stop minidom converting < > to &lt; &gt;
for tag in tags:
    tag_element = doc.createCDATASection(tag.thetag)
    tags_element.appendChild(tag_element)
