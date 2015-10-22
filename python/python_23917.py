# Passing variables to templates in Django
context = {"is_canner": is_canner}
return render(request, 'cans/cans.html', context)
