# How to extract data in *.txt file and use it in Python?
with open('u.txt') as uf, open('v.txt') as vf:
    for u,v in zip(uf,vf):
        print uv2sd(float(u),float(v))
