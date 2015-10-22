# Python Regex combined with string substitution?
match = re.search (r'^\[(\d+)\] (SERVICE NOTIFICATION:).*(\bCRITICAL).*(%s)'
                    % options.hostname, line)
