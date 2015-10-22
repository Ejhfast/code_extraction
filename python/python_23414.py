# make os.listdir() list complete paths
files = sorted(os.listdir('dumps'), key=lambda fn:os.path.getctime(os.path.join('dumps', fn)))
