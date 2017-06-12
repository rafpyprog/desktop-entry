from desktopentry.posix.specification import Group

class Group():
    def __init__(self, group_name, is_extension=True, allowed_keys, **kwargs):
        ''' Generic element to handle Desktop Entries elements
            :group_name:
            :is_extension: boolean indicating if the group follows the DES-EMA
                           from nautilus-actions.
            :allowed_keys: key.keychain with the allowed keys for the group,
                           according to the Desktop Entry Specification.
                           It will be user to validate the kwargs.
            :kwargs: keys to assign to the element being created.
        '''
        self.group_name = self.get_group_name(group_name)
        self.is_extension = is_extension
        self.kwargs = kwargs
        self.allowed_keys = allowed_keys
        self.check_required_keys(kwargs)

        for key in kwargs:
            if key not in self.allowed_keys:
                msg = '{} is not a valid key for this element.'.format(key)
                raise ValueError(key)
            else:
                setattr(self, key, kwargs[key])

    def get_group_name(self, name):
        if hasattr(Group, name):
            return name
        else:
            msg = '{} is not a valid groupname.'
            raise AttributeError(msg)

    @property
    def get_group_type(self):
        if self.is_extension and self.group_name == Group.DESKTOP_ENTRY.name:
            return 'Action'
        else:
            return self.kwargs[group_type]


    @property
    def required_keys(self):
        return self.get_required_keys()

    @property
    def groupname(self):
        return self.get_groupname()

    def get_groupname(self):

    def get_required_keys(self):
        ''' Get the required keys for this element. '''
        required_keys = []
        for key in self.allowed_keys:
            if self.allowed_keys[key].is_required:
                required_keys.append(key)
        return required_keys

    def check_required_keys(self, kwargs):
        ''' Check if all the required element keys were provided. '''
        for key in self.required_keys:
            if key not in kwargs:
                msg = 'Required key "{}" not assigned.'.format(key)
                raise AttributeError(msg)
