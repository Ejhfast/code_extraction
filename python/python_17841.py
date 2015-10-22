# get_template_attribute() - how to inject template globals
app.jinja_env.globals.update(global_key1=global_value1,
                             global_key2=global_value2,
                             global_key3=global_value3)
