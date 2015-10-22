# Mako, use if / else control structure in one line
text = 'Rappel de paimenet' if object.lang == 'fr_FR' else 'Payment reminder'
# Now your template doesn't need to use an if-statement
template = Template("""Status: {{text}}""").render(text=text)
