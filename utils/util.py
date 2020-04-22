import pickle

def pickle_it(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def unpickle_it(file):
    with open(file, 'rb') as f:
        return pickle.load(f)
