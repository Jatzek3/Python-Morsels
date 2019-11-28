class EasyDict:
    def __init__(self, _dict={}):
        self.__dict__.update(_dict)

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

