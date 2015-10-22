# How to loop through one element of a zip() function twice - Python
for image in folderToResizeContents:
    for fmt in sizeFormats:
        (w,h) = fmt.split('x')
