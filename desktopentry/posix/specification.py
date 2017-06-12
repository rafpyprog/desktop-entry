from .key import KeyElement, KeyChain, KeyType



class Group(object):
    '''
    Set of supported Group names. The PROFILE comes from the DES-EMA from
    nautilus-actions.
    '''
    DESKTOP_ENTRY = {'header': '[Desktop Entry]'}
    ACTION = {'header': 'Desktop Action {}'}
    PROFILE = {'header': '[X-Action-Profile {}]'}  # DES-EMA


ActionRequiredEntries = KeyChain(
    name=KeyElement('Name', LOCALESTRING, True),
    profiles=KeyElement('Profiles', STRINGS_LIST, True),
    )
