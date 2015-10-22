# Why does my image not appear?
if image:
        if image.primary_image:
            url = images.get_serving_url(str(image.primary_image.key()))
