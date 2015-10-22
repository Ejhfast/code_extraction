# Formatting PyYAML dump() output
stream = yaml.dump(list_of_dicts, default_flow_style = False)
file.write(stream.replace('\n- ', '\n\n- '))
