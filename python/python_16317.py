# What is the best possible way to calculate the sum of digits of a number?
int num = 1234;
double sum = num.ToString().Sum(s =&gt; Char.GetNumericValue(s));
