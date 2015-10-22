# How to encode all values in the dict?
{k:v.encode('utf-8') if isinstance(v, basestring) else v for k,v in d.items()}
