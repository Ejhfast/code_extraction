# webpy template with session - ThreadedDict error
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'username': 'test_user'})
