# How can a list comprehension do this
dist_lines = [{'cost_center': ccdl.analytic_id.code,
               'destination': ccdl.destination_id.code}
              for ccdl in ccdl_rows]
