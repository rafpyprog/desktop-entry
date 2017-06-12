#! /usr/local/bin/python3.6


from desktopentry.posix.key import KeyElement, KeyChain, KeyType
from collections import UserDict

BOOLEAN = KeyType.boolean
LOCALESTRING = KeyType.localestring
STRING = KeyType.string
STRINGS_LIST = KeyType.stringslist


class Keys(UserDict):
    def __init__(self, **kwargs):
        self.data = kwargs
        self.setter()

    def setter(self):
        for key in self.data:
            setattr(self, str(key), self.data[key])


ActionKeys = KeyChain(
    description        = KeyElement('Description', LOCALESTRING, False),
    enabled            = KeyElement('Enabled', BOOLEAN, False),
    entry_type         = KeyElement('Type', STRING, False),
    hidden             = KeyElement('Hidden', BOOLEAN, False),
    icon               = KeyElement('Icon', LOCALESTRING, False),
    name               = KeyElement('Name', LOCALESTRING, True),
    profiles           = KeyElement('Profiles', STRINGS_LIST, True),
    suggested_shortcut = KeyElement('SuggestedShortcut', STRING, False),
    target_context     = KeyElement('TargetContext', BOOLEAN, False),
    target_location    = KeyElement('TargetLocation', BOOLEAN, False),
    target_toolbar     = KeyElement('TargetToolbar', BOOLEAN, False),
    toolbar_label      = KeyElement('ToolbarLabel', LOCALESTRING, False),
    tooltip            = KeyElement('Tooltip', LOCALESTRING, False))


class Element():
    def __init__(self, element_keys, **kwargs):
        self.element_keys = element_keys
        self.check_required_keys(kwargs)

        for key in kwargs:
            if key not in self.element_keys:
                msg = '{} is not a valid key for this element.'.format(key)
                raise ValueError(key)
            else:
                setattr(self, key, kwargs[key])

    @property
    def required_keys(self):
        required_keys = []
        for key in self.element_keys:
            if self.element_keys[key].is_required:
                required_keys.append(key)
        return required_keys

    def check_required_keys(self, kwargs):
        for key in self.required_keys:
            if key not in kwargs:
                msg = 'Required key "{}" not assigned.'.format(key)
                raise AttributeError(msg)
