# Is there a builtin "hash to string" in Perl?
use Data::Dumper;
local $Data::Dumper::Terse = 1;
my $str = Dumper({a =&gt; 1, b =&gt; 2, c =&gt; 3});
