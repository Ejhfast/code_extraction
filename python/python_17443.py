# PJSUA --null-audio for python bindings
lib = pj.Lib()
lib.init(log_cfg=pj.LogConfig(level=3, callback=log_cb))
lib.set_null_snd_dev()
