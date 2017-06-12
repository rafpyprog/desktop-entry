from collections import UserDict
from .key import KeyElement, KeyChain, KeyType

BOOLEAN = KeyType.boolean
LOCALESTRING = KeyType.localestring
STRING = KeyType.string
STRINGS_LIST = KeyType.stringslist

ProfileKeys = KeyChain(
    name             = KeyElement('Name', LOCALESTRING, False},
    exec             = KeyElement('Exec', STRING, True),
    path             = KeyElement('Path', STRING, False),
    execution_mode   = KeyElement('ExecutionMode', STRING, False),
    startup_notify   = KeyElement('StartupNotify', BOOLEAN, False),
    startup_WM_class = KeyElement('StartupWMClass', STRING, False),
    execute_as       = KeyElement('ExecuteAs', STRING, False)
    )

class Profile():
    def __init__(self, exec, **kwargs):
        '''
            Exec:. command to execute, possibly with arguments. Paramentes
                   may apper in Exec value.
        '''
        # set the default attributes
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        for i in args[1:]:
            setattr(self, i, values[i])

        self._header = None
        self.header = self.Name
        self.conditions = conditions
        self.set_conditions()

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = "[X-Action-Profile {}]".format(value)

    def set_conditions(self):
        for i in self.conditions:
            print(i)
