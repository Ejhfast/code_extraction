# splitting strings after certain characters
SPLIT="SV="
line="&gt;tr|A0A024RAP8|A0A024RAP8_HUMAN HCG2009644, isoform CRA_b OS=Homo sapiens GN=KLRC4-KLRK1 PE=4 SV=1MGWIRGRRSRHSWEMSEFHNYNLDLKKSDFSTRWQ"
print line.split(SPLIT)[0] + SPLIT + line.split(SPLIT)[1][0]
