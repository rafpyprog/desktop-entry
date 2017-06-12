from collections import UserDict


class EntryType():
    ''' The value types recognized are string, localestring, boolean,
        numeric and stringslist

    - Values of type string may contain all ASCII characters except for
      control characters.
    - Values of type localestring are user displayable, and are encoded
      in UTF-8.
    - Values of type boolean must either be the string true or false.
    - Values of type numeric must be a valid floating point number as
      recognized by the %%f specifier for scanf in the C locale.
    - Values of type stringslist must be a string with items separeted by a
      semicolon.
    '''
    BOOLEAN = 'BOOLEAN'
    LOCALESTRING = 'LOCALESTRING'
    NUMERIC = 'NUMERIC'
    STRING = 'STRING'
    STRING_LIST = 'STRING_LIST'


class Entry():
    def __init__(self, key, key_type):
        '''
        key_type: boolean, localestring, string
        '''
        self.key = key
        self.set_key_type(key_type)

    def set_key_type(self, value):
        if hasattr(EntryType, value):
            self.entry_type= value
        else:
            raise ValueError('"{}" is not a valid key type.'.format(value))


class EntriesGroup(UserDict):
    def __init__(self, **kwargs):
        self.data = kwargs
        self.setter()

    def setter(self):
        for key in self.data:
            if isinstance(self.data[key], Entry):
                setattr(self, str(key), self.data[key])
            else:
                raise TypeError("{} is not a key.Entry instance.".format(key))


Entries = EntriesGroup(
    actions            = Entry('Actions', EntryType.STRING_LIST),
    categories         = Entry('Categories', EntryType.STRING_LIST),
    comment            = Entry('Comment', EntryType.STRING),
    dbus_activatable   = Entry('DBusActivatable', EntryType.BOOLEAN),
    description        = Entry('Description', EntryType.LOCALESTRING),
    enabled            = Entry('Enabled', EntryType.BOOLEAN), # Whether the item is candidate to be displayed in the context menu.
    group_type         = Entry('Type', EntryType.STRING),
    exec_command       = Entry('Exec', EntryType.STRING),
    generic_name       = Entry('GenericName', EntryType.STRING),
    hidden             = Entry('Hidden', EntryType.BOOLEAN),
    icon               = Entry('Icon', EntryType.LOCALESTRING),
    implements         = Entry('Implements', EntryType.STRING_LIST),
    keywords           = Entry('Keywords', EntryType.STRING_LIST),
    mime_type          = Entry('MimeType', EntryType.STRING_LIST),
    name               = Entry('Name', EntryType.LOCALESTRING),  #The label of the action, as it should appear in the context menu.
    no_display         = Entry('NoDisplay', EntryType.STRING),
    not_show_in        = Entry('NotShowIn', EntryType.BOOLEAN),
    only_show_in       = Entry('OnlyShowIn', EntryType.BOOLEAN),
    path               = Entry('Path', EntryType.STRING),
    startup_notify     = Entry('StartupNotify', EntryType.STRING),
    startup_WM_class   = Entry('StartupWMClass', EntryType.STRING),
    suggested_shortcut = Entry('SuggestedShortcut', EntryType.STRING),
    target_context     = Entry('TargetContext', EntryType.BOOLEAN),
    target_location    = Entry('TargetLocation', EntryType.BOOLEAN),
    target_toolbar     = Entry('TargetToolbar', EntryType.BOOLEAN),
    terminal           = Entry('Terminal', EntryType.BOOLEAN),
    toolbar_label      = Entry('ToolbarLabel', EntryType.LOCALESTRING),
    tooltip            = Entry('Tooltip', EntryType.LOCALESTRING),  # The tooltip associated with the item in the context menu.
    try_exec           = Entry('TryExec', EntryType.STRING),
    url                = Entry('URL', EntryType.STRING),
    version            = Entry('Version', EntryType.STRING),
    # DES-EMA keys
    execute_as         = Entry('ExecutionAs', EntryType.STRING),  # 	The user the command must be ran as. The user may be identified by its numeric UID or by its login.
    execution_mode     = Entry('ExecutionMode', EntryType.STRING),  # Execution mode of the program called by the profile.
    items_list         = Entry('ItemsList', EntryType.STRING_LIST),  # The ordered list of the subitems (actions or menus) attached to a menu.
    mime_types         = Entry('MimeType', EntryType.STRING_LIST),
    profiles           = Entry('Profiles', EntryType.STRING_LIST), # The ordered list of the profiles attached to this action.
    show_if_registered = Entry('ShowIfRegistered', EntryType.STRING), # The well-known name of a DBus service.
    show_if_true       = Entry('ShowIfTrue', EntryType.STRING),
    show_if_running    = Entry('ShowIfRunning', EntryType.STRING),
    basenames          = Entry('Basenames', EntryType.STRING_LIST),
    matchcase          = Entry('Matchcase', EntryType.BOOLEAN),  # Whether the above Basenames is case sensitive.
    selection_count    = Entry('SelectionCount', EntryType.STRING),  # Whether this profile may be selected depending of the count of the selection.
    schemes            = Entry('Schemes', EntryType.STRING_LIST),
    folders            = Entry('Folders', EntryType.STRING_LIST),  # A list of paths the current base directory must be in in order the item be selected.
    capabilities       = Entry('Capabilities', EntryType.STRING_LIST), #A list of capabilities each item of the selection must satisfy in order the item be candidate.
    )
