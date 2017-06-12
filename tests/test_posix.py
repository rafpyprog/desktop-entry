import os
import sys


import pytest

from desktopentry.posix import action
from desktopentry.posix import profile
from desktopentry.posix import storelocation
from desktopentry.posix.key import KeyChain, KeyElement

'''
    Store location tests
'''
def test_store_location():
    location = storelocation.define_store_location()

    DESKTOP_FILE_DIR = os.path.join('file-manager', 'actions')
    default = os.path.join(os.path.expanduser('~'), '.local', 'share')
    xdg_data_home = os.getenv('XDG_DATA_HOME', default)
    expected_location = os.path.join(xdg_data_home, DESKTOP_FILE_DIR)

    assert location == expected_location


def test_store_location_is_dir():
    location = storelocation.define_store_location()
    assert os.path.isdir(location) is True


'''
 profile.py
'''



'''
    Action
'''
# ActionKeys
def test_action_keys_count():
    specification_count = 13
    keys_count = len(action.ActionKeys)
    assert specification_count == keys_count


def test_action_keys_is_chain():
    assert isinstance(action.ActionKeys, KeyChain) is True


def test_action_keys_are_key_element_and_attributes():
    action_keys = action.ActionKeys
    for key in action_keys:
        assert isinstance(action_keys[key], KeyElement)
        assert hasattr(action_keys, key)
