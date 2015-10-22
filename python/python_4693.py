# How to hide console window on Windows when using scons-qt4 plugin?
if (env ['PLATFORM'] == 'win32'):
    env.Append (LINKFLAGS = ['-Wl,-subsystem,windows'])
