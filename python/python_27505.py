# Aggregate records with peewee and Python
MF_Logg.select(fn.SUM(MF_Logg.Logg_Giva_Foder1)) \
    .where((MF_Logg.Logg_RFID_ID == tag_no) &amp; (MF_Logg.Logg_Tid &gt; timelastday)) \
    .scalar()
