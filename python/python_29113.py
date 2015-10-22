# Flask, Python and Socket.io: multithreading app is giving me "RuntimeError: working outside of request context"
def someotherfunction():
    with app.test_request_context('/'):
        emit('anEvent', jsondata, namespace='/test')
