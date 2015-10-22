# bottle template not found ( Error 500 )
def GET_Contents(filepath):
    return os.listdir(os.path.join('files', filepath))
