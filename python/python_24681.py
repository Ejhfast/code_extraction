# In python is there a way to patch a list similiar to using patch.dict?
with patch.object(integrations, 'PARTNERS',[partner_type]):
    self._do_stuff()
