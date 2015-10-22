# how to round up a complex no(1.9999999999999998-2j) as (2-2j) in python
&gt;&gt;&gt; num = 1.9999999999999998-2j
&gt;&gt;&gt; round(num.real, 2) + round(num.imag, 2) * 1j
(2-2j)
