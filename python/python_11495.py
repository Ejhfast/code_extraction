# Memory efficient import many data files into panda DataFrame in Python
dir_path = os.path.join(data_dir, 'master_*.dat')
master_all = pd.concat(pd.read_table(data_file, delimiter='|', header=0)
                                     for data_file in glob.glob(dir_path))
