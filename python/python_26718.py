# Remove everything between second and second last occurance of match
perl -pE's/;.*?\K;.*(?=;.*;)//' &lt;&lt;&lt;'cellular organisms;Eukaryota;Opisthokonta;...;Tribolium;Tribolium castaneum;'
