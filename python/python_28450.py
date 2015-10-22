# returning values from matlab to python (as a dictionary?)
function out = mymatlabfunc(x,y)
    # compute stuff
    out = struct('interesting variable 1', x_out, 'interesting variable 2', y_out, ...);
