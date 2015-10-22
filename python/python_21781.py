# Segfault at err() (from err.c) when called from python ctypes
if(count &gt; MAX_PREFIXES)
    err(MAX_PREFIXES, "too many prefixes (%i &gt; %i)", count, MAX_PREFIXES);
