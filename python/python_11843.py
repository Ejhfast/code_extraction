# pass kwargs to re.sub()
return m.sub(partial(process_pseudo_ternary, custom_1=True, custom_2=True), ts)
