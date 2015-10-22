# Python - write/ADD a new record in file with Json format
data['added_data'] = 'some data added'
 write_file = open("/home/sage/content.txt", "w")
 write_file.write(json.dumps(data))
