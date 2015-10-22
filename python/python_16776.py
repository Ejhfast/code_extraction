# Scons - using custom preprocessor with scons cache
out_cc = env.Command('file.wave.cpp', 'file.cpp', 'wave command &lt; $SOURCE &gt; $TARGET')
env.Program('myprog', ['this.cc', 'that.cc', out_cc])
