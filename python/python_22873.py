# Loading all objects of a dictionary from a pickle file
def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, -1)
