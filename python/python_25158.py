# python formula get value from another sheet have space with python
sheet.write_merge(0, 0, 5, 8, xlwt.Formula("""IF('Original Data'!B4&lt;&gt;"",'Original Data'!B4,"")"""), center)
