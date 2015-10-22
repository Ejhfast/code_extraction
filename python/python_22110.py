# PyMYSQL query not returning desired results
cursor.execute("""SELECT Named_Insured_First_Name, Named_Insured_Last_Name FROM condo_rented_to_others WHERE Named_Insured_First_Name=%s AND Named_Insured_Last_Name=%s """, (user_input_fname, user_input_lname,))
