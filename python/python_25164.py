# Writing itertools results to csv output
f=open('foo.csv','w')
f.write('\n'.join(",".join(seq) for seq in itertools.product("01", repeat=10)))
f.close()
