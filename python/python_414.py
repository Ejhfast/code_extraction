# Is there a way to get all the directories but not files in a directory in Python?
def listfiles(directory):
    return [f for f in os.listdir(directory)
              if os.path.isdir(os.path.join(directory, f))]
