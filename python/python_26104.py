# csv Jinja2 template render unicode error
fh.write(template.render(row).encode('utf8'))
