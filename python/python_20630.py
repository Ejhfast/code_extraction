# Django, Display uploaded image URL in template
def productpage(request, product_image_id):
    product = get_object_or_404(Image, product_image=product_image_id)
    render(request, 'polls/productpage.html', {'product': product})
