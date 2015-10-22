# How do i set the max size for an image in Reportlab, without rescaling?
def create_logo(absolute_path):
    image = Image(absolute_path)
    image._restrictSize(2 * inch, 1 * inch)
