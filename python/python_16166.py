# Shell script to Search and Export to csv file/Excel sheet
awk 'BEGIN{print "WAM"}/\&lt;WAM\&gt;/{print $1}' /home/santosh/messages &gt; text.file
