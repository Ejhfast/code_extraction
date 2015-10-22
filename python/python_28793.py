# Kivy - How to make an object accessible from both Kv Language child widgets and Python widget's classes?
class MyLayout(BoxLayout):
    def getPerson1Name(self):
        return App.get_running_app().person2.getName()
