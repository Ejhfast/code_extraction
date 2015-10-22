# Editing MS Word header with win32com
word.ActiveDocument.Sections(1).Headers(win32.constants.wdHeaderFooterPrimary).Range.Text='test text'
