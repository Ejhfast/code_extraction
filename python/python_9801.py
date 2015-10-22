# Tornado application layout. Options.
import tornado.options
tornado.options.parse_config_file("/etc/server.conf")
tornado.options.parse_command_line()
