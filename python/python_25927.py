# Apache Pig - How to maintain a distributed look-up table for my python UDF to access?
A = LOAD 'data1' USING ... AS ...;
B = LOAD 'lookuptable' USING ... AS ...;
C = JOIN A BY join_key, B BY join_key USING 'replicated';
