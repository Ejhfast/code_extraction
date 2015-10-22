# How to handle web and mobile requests in django view
class YourView(generics.TypOfView):
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer,)
    template_name = 'path_to_template.html'
