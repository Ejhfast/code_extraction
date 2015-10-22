# How to parse C array in python
[re.sub("/\*.+\*/", "", m).replace('\n', '').strip() for m in re.findall("{(.+?)};", c_file_as_string, re.S)]
