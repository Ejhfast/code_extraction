# Find if dates are overlapping in a list of N pairs
def test_overlap(dt1_st, dt1_end, dt2_st, dt2_end):
    return not (dt1_st &lt; dt2_end and dt1_end &gt;dt2_st)
