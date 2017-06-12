from collections import UserDict
from .key import KeyElement, KeyChain, KeyType

BOOLEAN = KeyType.boolean
LOCALESTRING = KeyType.localestring
STRING = KeyType.string
STRINGS_LIST = KeyType.stringslist

# Valid keys for Action definition
ActionKeys = KeyChain(
    description        = KeyElement('Description', LOCALESTRING, False),
    enabled            = KeyElement('Enabled', BOOLEAN, False),
    group_type         = KeyElement('Type', STRING, False),
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


class Action():
    def __init__(self, name, profiles, **kwargs):
        # Required keys
        self.name = name
        self.set_profiles(profiles)

        # Optional keys
        for key in kwargs:
            if key in ActionKeys:
                setattr(self, arg, kwargs[arg])
            else:
                raise ValueError('"{}" is not a valid key.'.format(key))

    @property
    def profile_text(self):
        delimiter = "; "
        return delimiter.join([p.Name for p in self.Profiles])

    def add_profile(self, profile):
        '''Add a Profile to the Action's profiles
        Args:
            profile(list, Profile): the profile(s) to add

        Returns:
            None
        '''
        new_profiles = ""
        if isinstance(profile, list):
            is_valid = all([isinstance(p, Profile) for p in profile])
            if is_valid:
                for new_profile in profile:
                    self.set_profiles(new_profile)
            else:
                raise TypeError('Profile is not a Profile Class instance.')
        elif isinstance(profile, Profile):
            self.set_profiles(profile)
        else:
            raise TypeError('Profile is not a Profile Class instance.')

    def set_profiles(self, profile):
        if hasattr(self, 'Profiles'):
            self.Profiles.append(profile)
        else:
            self.Profiles = [profile]
