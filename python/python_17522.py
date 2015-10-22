# Python runtime_library_dirs doesn't work on Mac
if platform.system() == 'Darwin':
    extra_link_args.append('-Wl,-rpath,'+lib_path)
