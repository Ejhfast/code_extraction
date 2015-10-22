# python mmap flush() doesn't work with ACCESS_COPY
if (self-&gt;access == ACCESS_READ || self-&gt;access == ACCESS_COPY)
    return PyLong_FromLong(0);
