# Flask SocketIO send message from server to room
socketio.emit('my response', {'data': json.dumps(my_info, ensure_ascii=False)}, room=room, namespace='/test')
