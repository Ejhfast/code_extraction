# Lambda function and variable scope
for control in self.controls():
  self.connect(control, SIGNAL('clicked()'), lambda control=control:
    self.button(control.objectName()))
