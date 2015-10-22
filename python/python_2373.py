# Django select max id
Image.objects.all().order_by("-id")[0]
