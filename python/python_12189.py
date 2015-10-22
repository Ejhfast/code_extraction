# translate a mixed fasta file using python/biopython
if all(c.upper() in 'ATGC' for c in seq_record.seq):
    pass # it's DNA
