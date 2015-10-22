# UnicodeEncodeError in Mako Template
template = Template(filename='../template/dummy.html', default_filters=['decode.utf8'], input_encoding='utf-8', output_encoding='utf-8')
