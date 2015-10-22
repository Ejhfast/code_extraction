# GIO: get_icon() always returns None
f = File.new_for_commandline_arg('...')
info = f.query_info('standard::icon')
print(info.get_icon())
