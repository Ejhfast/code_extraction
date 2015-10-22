# Grako end closure when rule is matched
def_body = 'def' name:name args:{name !'+'} body:expression;
