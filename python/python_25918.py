# echo json to textfile removes double quotes
("echo %s &gt; /home/user/%s" % (simplejson.dumps(d), 'textfile')).replace('"', '\\"')
