# flask-login session gets destroyed on every apache restart
@login_manager.user_loader
def load_user(id):
    return "get the user properly and create the usermixin object"
