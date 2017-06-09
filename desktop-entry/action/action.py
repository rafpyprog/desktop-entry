Keys = UserDict(
    description='Description',
    enables='Enabled',
    entry_type='Type',
    hidden='Hidden',
    icon='Icon',
    name='Name',
    profiles='Profiles'
    suggested_shortcut='SuggestedShortcut',
    target_context='TargetContext',
    target_location='TargetLocation',
    target_toolbar='TargetToolbar',
    toolbar_label='ToolbarLabel',
    tooltip='Tooltip',
)


class Action():
    def __init__(self, name, profiles, entry_type='Action', tooltip=None,
                 icon=None, description=None, suggested_shortcut=None,
                 enabled=True, hidden=False, target_context=True,
                 target_location=False, target_toolbar=False,
                 toolbar_label=None, **conditions):
        ''' Defines how actions are to be described in .desktop files.

            To be valid, an action must have a non-empty name, and at least
            one Profile must be found valid at runtime.

            An action might be defined as a group of several elements:
            - the displayable part: label, tooltip, icon
            - conditions which have to be met in order the item be actually
              displayed in the context menu; these conditions are checked
              against the current file manager selection; these might be
              mimetypes, scheme, etc.
            - the command to be executed, and its parameters.

            An action may embed its own conditions. If these conditions are
            not met at runtime, then profiles are not even considered.
        '''
        self.Name = Name
        self.add_profile(Profiles)
        if ToolbarLabel is None:
            self.ToolbarLabel = self.Name

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
