# When add four parameter of values, annotate sum not work
cursor = connections["mam"].cursor()
cursor.execute("SELECT B.name, A.category_id, A.brand_id, SUM(A.answer) AS total, C.name FROM category_answers A INNER JOIN category B ON A.category_id = B.id INNER JOIN brand C ON A.brand_id = C.id WHERE A.brand_id = %s AND A.category_id = %s AND B.segment_category_id = %s", [cat["brand"],cat["category"],cat["category__segment_category"]])
c_answers = cursor.fetchone()
