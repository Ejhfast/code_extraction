# Python nested dictionary comprehension returns empty dictionaries
&gt;&gt;&gt; {k: {8: v[8]} for k, v in data_dict.items() if 8 in v}
{'three': {8: 'h'}}
