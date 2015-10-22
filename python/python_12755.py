# Converting User Item Rating Into Matrix Market Input format using Matlab or Python
fid = fopen('exp.txt');
A = fscanf(fid, '%d|%d|%g', [3 inf]);
S = sparse(A(1,:), A(2,:), A(3,:))
