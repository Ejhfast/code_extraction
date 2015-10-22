# Scale python kivy line
from kivy.core.window import Window
with self.canvas:
    self.translate = Translate(Window.width / 2, Window.height / 2.)
