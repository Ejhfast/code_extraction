# How to parse YouTube XML using Python?
for node in entry:
    video_title = node.getElementsByTagName('title')[0].firstChild.nodeValue
    print video_title
