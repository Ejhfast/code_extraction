# Python 2.7: execute sql query
cur.execute("SELECT p_p_t " +
                    "FROM q_r_f_d WHERE r_f_i = ?", (rfId,))
                                                       # ^
