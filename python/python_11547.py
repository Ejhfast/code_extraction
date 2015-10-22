# Why do two different equality tests between two strings of same length take different amounts of time
if (ref(a) == ref(b)) return true;
if (len(a) != len(b)) return false;
return compare_actual_data(a, b);
