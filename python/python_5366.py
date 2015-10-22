# multiple d-bus session bus objects in python
bus1 = dbus.bus.BusConnection("tcp:host=192.168.0.1,port=1234")
bus2 = dbus.bus.BusConnection("tcp:host=192.168.0.2,port=1234")
