# Elements in Tuple to Tuples in Bag Pig
a2 = foreach  generate a time, id_no, TOKENIZE($2);
