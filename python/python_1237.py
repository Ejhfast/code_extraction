# How to escape characters in Pango markup?
import cgi
print "&lt;span size='medium'&gt;&lt;b&gt;%s&lt;/b&gt;&lt;/span&gt;\n%s" %
      (cgi.escape(site_title), cgi.escape(URL))
