# python function *args and **kwargs with other specified keyword arguments
def set_axis(self, *args, **kwargs):
    xlabel = kwargs.get('xlabel', 'x')
    ylabel = kwargs.get('ylabel', 'y')
