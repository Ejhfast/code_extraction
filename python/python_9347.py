# check hostnames and IP addresses (v4 and v6) using a single python regex?
if ( $foo =~ /$ipv4_re/ or $foo =~ /$ipv6_re/ or $foo =~ /$hostname_re/ ) {
    ...
}
