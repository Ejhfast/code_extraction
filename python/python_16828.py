# How can I listen for changes in one plot's traits and update the second by that amount?
on_trait_change(self.lineplot.value, self._handle_data_change, name="data_changed")
