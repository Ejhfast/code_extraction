# Circular import in python+django?! how to make it work?
class Art2C(..):
    art = m.ForeignKey('Article')
    from_other_app = m.ForeignKey('other_app.Article')
