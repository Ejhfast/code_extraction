# Converting PIL Image to GTK Pixbuf
import numpy
arr = numpy.array(im)
return gtk.gdk.pixbuf_new_from_array(arr, gtk.gdk.COLORSPACE_RGB, 8)
