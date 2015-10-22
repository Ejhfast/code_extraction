# TypeError: sequence item 0: expected str instance, int found
def  lekToString(lek):
return '|'.join([str(lek['ser_br']), str(lek['fab_naziv']), str(lek['gen_naziv']), str(lek['c_leka']), str(lek['kol_leka'])])
