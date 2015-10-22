# Listing all patterns that a regex matches
perl -E '$_ = 'Mastering Regular Expressions'; /(\p{L}*)(?{ say qq![$^N]! })(?!)/g;'
