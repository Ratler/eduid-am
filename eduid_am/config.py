import os
import os.path
import ConfigParser


DEFAULT_CONFIG_FILE_NAME = 'eduid_am.ini'


def get_config_file():
    """Get the configuration file looking for it in several places.

    The lookup order is:
    1. A file named acording to the value of the EDUIM_AM_CONFIG env variable
    2. A file named eduid_am.ini In the current working directory
    3. A file named .eduim_am.ini in the user's home directory
    4. A file named eduim_am.ini in the system configuration directory
    """
    file_name = os.environ.get('EDUID_AM_CONFIG', DEFAULT_CONFIG_FILE_NAME)

    if os.path.exists(file_name):
        return file_name

    user_file = os.path.expanduser(
        os.path.join('~', '.', DEFAULT_CONFIG_FILE_NAME))
    if os.path.exists(user_file):
        return user_file

    global_file = os.path.join('/etc', DEFAULT_CONFIG_FILE_NAME)
    if os.path.exists(global_file):
        return global_file


def read_configuration():
    """
    Read the settings from environment or .ini file and return them as a dict
    """
    settings = {}

    config = ConfigParser.RawConfigParser()

    config_file = get_config_file()
    if config_file is not None:
        config.read(config_file)

        if config.has_section('main'):
            settings = dict([(s.upper(), v) for s, v in config.items('main')])

    return settings
