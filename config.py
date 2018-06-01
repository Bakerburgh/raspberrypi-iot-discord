import configparser
import os


def load(filename: str):
    return Config(filename)


class Config:

    default_config = 'default.ini'

    def __init__(self, config_filename: str):
        if not os.path.isfile(config_filename):
            raise FileNotFoundError("Could not find config file '{0}'".format(config_filename))
        config_abs = os.path.abspath(config_filename)

        # Load the default settings
        basepath = os.path.dirname(__file__)
        defconfig_abs = os.path.join(basepath, self.default_config)
        parser = configparser.ConfigParser()
        parser.read(defconfig_abs)

        # Load the custom config file
        parser.read(config_abs)

        discord_config = parser['discord']
        self.discord_token = discord_config.get('token')
        self.discord_server = discord_config.get('server')
        self.discord_channel = discord_config.get('channel')
        self.discord_description = discord_config.get('description')
        self.discord_prefix = discord_config.get('prefix')


