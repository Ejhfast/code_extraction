# How to download a Excel file from behind a paywall into a pandas dataframe?
with io.BytesIO(r.content) as fh:
    df = pd.io.excel.read_excel(fh, sheetname=0)
