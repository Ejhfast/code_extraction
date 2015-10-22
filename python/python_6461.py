# How to replace all occurrences of X between Y's?
$str = 'smth Y1 test X foo X Y2 bar X Y1 X X Y2';
$str =~ s/X(?=((?!Y1).)*Y2)/Z/g;
print $str; #smth Y1 test Z foo Z Y2 bar X Y1 Z Z Y2
