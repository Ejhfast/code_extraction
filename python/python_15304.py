# Automatic binding using lambdas inside a loop
self.top.bind(binding, lambda event, action=action: self.callback(event, self.actionRep.__class__.__dict__[action]))
