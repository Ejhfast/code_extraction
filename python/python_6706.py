# Form validation and MultiValueDictKeyError
logs = 0
if request.POST.get and 'logs' in request.POST and request.POST['logs'] == "on":
    logs = 1
