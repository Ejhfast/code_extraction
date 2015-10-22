# python regex strips out backslash
newContent = re.compile(varRegEx, re.VERBOSE).sub(r'\1%s'%valStr.replace('\\', '\\\\'), cmdFileContent)
