import argparse


class CliArgs:
    def __init__(self):
        parser = argparse.ArgumentParser(description='A Discord bot to interface with this device.')
        parser.add_argument('config', help='Configuration file')

        args = parser.parse_args()

        self.config_filename = args.config
