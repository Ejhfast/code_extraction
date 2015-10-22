# In python - Find the maximum date in a nested dictionary
max(my_dict.items(), key=lambda x: x[1]['last_event'])[0]
