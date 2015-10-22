# django form widget rendering
def format_output(self, rendered_widgets):
        return u'%s - %s - %s' % \
            (rendered_widgets[0], rendered_widgets[1], rendered_widgets[2])
