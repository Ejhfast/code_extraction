# Swig, python and output strings
%include &lt;cstring.i&gt;
%cstring_output_allocate(char **str, free(*$1));
