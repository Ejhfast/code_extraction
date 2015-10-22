# python2.7 + multiprocessing + selenium: restart process on exception
def do_work(rsrt):
    if failed:
        return do_work(rsrt)
