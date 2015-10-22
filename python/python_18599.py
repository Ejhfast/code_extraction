# pyyaml is producing undesired !!python/unicode output
yaml.safe_dump(data, file(filename,'w'), encoding='utf-8', allow_unicode=True)
