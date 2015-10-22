# How do I execute a complex shell find command from Python?
subprocess.call(["find", ".", "-exec", "touch", "{}", ";"])
