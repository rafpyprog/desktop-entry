import os
from xdg.BaseDirectory import xdg_data_home, save_data_path


def define_store_location():
    '''
    According to the DES-EMA (http://www.nautilus-actions.org/?q=node/377)
    .desktop files are Searched for in "XDG_DATA_DIRS/file-manager/actions".

    This module install user specif versions of .desktop files, therefore, it
    uses ""$XDG_DATA_HOME/file-manager/actions" as defined in the XDG Base
    Directory Specifications.

    Still according to the XDG Specifications If $XDG_DATA_HOME is either not
    set or empty, a default equal to $HOME/.local/share should be used. '''

    # Returns xdg_data_home or default
    XDG_DATA_HOME = xdg_data_home

    DESKTOP_FILE_DIR = os.path.join('file-manager', 'actions')

    # Ensure desktop data dir exists
    store_location = save_data_path(DESKTOP_FILE_DIR)
    return store_location
