# Python regex, how to replace text between two words in a parapgraph?
new_text = re.sub(r'(?s)(Heading1)(.*?)(Heading2)', r"\1 replaced with python script \3", string)
