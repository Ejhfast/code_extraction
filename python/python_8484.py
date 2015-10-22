# PYTHON REGEXP to replace recognized pattern with the pattern itself and the replacement?
new_string = re.sub(r'\.(\d+\. )', '&lt;/p&gt;&lt;p style="text-align: justify;"&gt;\\1', old_string)
