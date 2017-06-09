Keys = UserDict(
    name='Name',
)
class Profile():
    def __init__(self, Exec, Name="", Path="%%d",
                 ExecutionMode=ExecutionMode['NORMAL'], StartupNotify="false",
                 StartupWMClass="", ExecuteAs="", **conditions):
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
