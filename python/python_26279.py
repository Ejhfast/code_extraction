# curl post request failing in the presence of special characters
newjson = json.loads(result.read().decode('utf-8').encode("ascii","xmlcharrefreplace"))
