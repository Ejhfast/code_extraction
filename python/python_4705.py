# Rewrite views.py without using locals()
def display_meta(request):
    meta = request.META.items()
    return render_to_response('meta.html', {"meta": meta})
