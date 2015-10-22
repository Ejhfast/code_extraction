# In erlang: How do I expand wxNotebook in a panel?
%% Main Sizer
  wxSizer:add(MainSizer, LeftPanel, [{proportion,0},{border, 2}, {flag,?wxEXPAND bor ?wxALL}]),
  wxSizer:add(MainSizer, RightPanel, [{proportion,1},{border, 2}, {flag,?wxEXPAND bor ?wxTOP bor ?wxRIGHT bor ?wxBOTTOM}]),
