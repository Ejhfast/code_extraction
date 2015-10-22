# swig numpy multiple matrix and array inputs
%apply (char *STRING, int LENGTH) {(char *xstr, int xL),(char *ystr, int yL)}
