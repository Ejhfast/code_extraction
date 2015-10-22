# django: passing parameters in URLConf
def mylogin(request):
    app = request.GET.get('app')
    ...
