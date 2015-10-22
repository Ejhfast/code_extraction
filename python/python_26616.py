# Fastest way to convert Python List with dictionaries to one dictionary
&gt;&gt;&gt; dict_list = [{123123:[0.45, 0.4]},{2332:[0.1, 9]}]
&gt;&gt;&gt; {key: item[key] for item in dict_list for key in item}
{123123: [0.45, 0.4], 2332: [0.1, 9]}
