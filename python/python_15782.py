# pyobjc as a subprocess communicating with main process via pipe doesn't work
p = Process(target=OSXstatusbaritem.start, args=(pipeUI,))
