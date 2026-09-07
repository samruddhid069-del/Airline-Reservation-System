import pickle
import os


def save_data(filename, data):

    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_data(filename):

    if not os.path.exists(filename):
        return []

    with open(filename, "rb") as f:
        return pickle.load(f)