# How to make a variable accessible across all pages in HTML / Template (Django)..?
if request.POST:
    request.SESSION['select_menu_value'] = request.POST.get('select_menu_value')
