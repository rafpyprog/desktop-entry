from collections import UserDict

class Keys(UserDict):
    def __init__(self, **kwargs):
        self.data = kwargs
        self.setter()

    def setter(self):
        for key in self.data:
            setattr(self, str(key), self.data[key])
