# custom blast db with NcbiblastxCommandline
blastx_cline = NcbiblastxCommandline(cmd='blastn', query="queryfile.fas", db="newtest.db", evalue=0.00000001, outfmt=5, out="opuntia.xml")
