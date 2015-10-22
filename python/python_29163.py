# Python & Pandas: iterate through rows to set value
pd_data['imdbRating'] = pd_data['omdb_info'].apply(lambda x: x['imdbRating'])
