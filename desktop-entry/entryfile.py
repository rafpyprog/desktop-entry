
ENTRY_TYPE_DESKTOP = 1
ENTRY_TYPE_DIRECTORY = 2
ENTRY_TYPES = (ENTRY_TYPE_DESKTOP, ENTRY_TYPE_DIRECTORY)

class DesktopEntryFile():
    def __init__(self, entry_type):
        self.entry_type = entry_type

    @property
    def entry_type(self):
        return self.entry_type

    @entry_type.setter
    def entry_type(self, value):
        if value not in ENTRY_TYPES:
            invalid_desktop_msg = 'Invalid desktop entry type.'
            raise ValueError(invalid_desktop_msg)
        else:
            self.entry_type = value
