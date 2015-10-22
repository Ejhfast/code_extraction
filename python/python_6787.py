# How to place a combobox in wxgrid (python)?
choice_editor = wx.grid.GridCellChoiceEditor(choices_list, True)
    grid.SetCellEditor(row, col, choice_editor)
