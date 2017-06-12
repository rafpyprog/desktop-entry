#! /usr/local/bin/python3.6

from desktopentry.posix.entry import Entry
from collections import UserDict
from desktopentry.posix.specification import Group


class GetElementEntries():
    def extension(group_name, group_type):
        if group_name == 'desktop' and group_type == 'action':
            required = ['group_type', 'profiles']
            allowed = ['name', 'tooltip', 'icon', 'description',
                       'suggested_shortcut', 'enabled', 'hidden',
                       'target_context', 'target_location', 'target_toolbar',
                       'toolbar_label']

        elif group_name == 'desktop' and group_type == 'menu':
            required = ['group_type', 'name', 'items_list']
            allowed = ['tooltip', 'icon', 'description', 'suggested_shortcut',
                       'enabled', 'hidden']

        elif group_name == 'profile':
            required = ['exec_command']
            allowed = ['name', 'path', 'execution_mode', 'startup_notify',
                       'startup_WM_class', 'execute_as']
        else:
            raise ValueError('Invalid group_name or group_type')

        return required, allowed

    def standard(group_name, group_type):
        if group_name == 'desktop' and group_type in ['Application', 'Directory']:
            required = ['group_type', 'name']
            allowed = ['version', 'generic_name', 'no_display', 'comment',
                       'icon', 'hidden', 'only_show_in', 'not_show_in',
                       'dbus_activatable', 'try_exec', 'exec_command', 'path',
                       'terminal', 'actions', 'mime_type', 'categories',
                       'implements', 'keywords', 'startup_notify',
                       'startup_WM_class', 'url']
        elif group_name == 'desktop' and group_type == 'Link':
            required = ['group_type', 'name', 'url']
            allowed = ['version', 'generic_name', 'no_display', 'comment',
                       'icon', 'hidden', 'only_show_in', 'not_show_in',
                       'dbus_activatable', 'try_exec', 'exec_command', 'path',
                       'terminal', 'actions', 'mime_type', 'categories',
                       'implements', 'keywords', 'startup_notify',
                       'startup_WM_class']
        elif group_name == 'action':
            required = ['name']
            allowed = ['icon', 'exec_command']
        else:
            raise ValueError('Invalid group_name or group_type')

        return required, allowed

GetElementEntries.extension()

def get_element_entries(group_name, group_type, is_extension):
    if is_extension:
        required, allowed = GetElementEntries.extension(group_name, group_type)
    else:
        required, allowed = GetElementEntries.des(group_name, group_type)



class Element():
    def __init__(self, group_name, is_extension, **kwargs):
        self.group_type = kwargs.get("group_type", None)
        if not group_type:
            pass # implementations should ignore desktop entries with an unknown type.
        else:
            required_entries, allowed_entries = get_entries(group_name, group_type, is_extension)
        '''
        groupname: desktop, action, profile
        is_extension: True or False
        '''
        self.groupname = groupname

        if is_extension:

        else:

        self.groupname = self.groupname
        self.required_keys = required_keys
        self.element_keys = element_keys
        self.check_required_keys(kwargs)

        for key in kwargs:
            if key not in self.allowed_keys:
                msg = '{} is not a valid key for this element.'.format(key)
                raise ValueError(key)
            else:
                setattr(self, key, kwargs[key])

    def check_required_keys(self, kwargs):
        for key in self.required_keys:
            if key not in kwargs:
                msg = 'Required key "{}" not assigned.'.format(key)
                raise AttributeError(msg)


action_required = ['']
