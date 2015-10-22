# Read From PowerPoint Table in Python?
For r = 1 to tbl.rows.count
   For c = 1 to tbl.columns.count
      tbl.cell(r,c).Shape.Textframe.Text ' is what you're after
