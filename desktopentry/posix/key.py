from collections import UserDict


class KeyType():
    localestring = 'localestring'
    string = 'string'
    stringslist = 'stringslist'
    boolean = 'boolean'


class KeyElement():
    def __init__(self, name, key_type, is_required):
        '''
        key_type: boolean, localestring, string
        '''
        self.name = name
        self.set_key_type(key_type)
        self.set_is_required(is_required)

    def set_is_required(self, value):
        if isinstance(value, bool):
            self.is_required = value
        else:
            raise TypeError("required is not a boolean.")

    def set_key_type(self, value):
        if hasattr(KeyType, value):
            self.key_type = value
        else:
            raise ValueError('"{}" is not a valid key type.'.format(value))


class KeyChain(UserDict):
    def __init__(self, **kwargs):
        self.data = kwargs
        self.setter()

    def setter(self):
        for key in self.data:
            if isinstance(self.data[key], KeyElement):
                setattr(self, str(key), self.data[key])
            else:
                raise TypeError("{} is not a key.KeyElement instance.".format(key))
