from os import path
from configparser import ConfigParser
from argparse import ArgumentParser

CONF_PATH = '{}/.config/youterm.conf'.format(path.expanduser("~"))

class YTConfig:
    def __init__(self):
        print(CONF_PATH)
        parser = ConfigParser()
        try:
            with open(CONF_PATH):
                pass
        except FileNotFoundError:
            self.create_conf()

        parser.read(CONF_PATH)
        self.dev = parser.get('video', 'device')
        self.token = parser.get('api', 'token')
    
    def create_conf(self):
        '''
            Create the default configuration file in the users
            .config directory
        '''
        writer = ConfigParser()
        writer.add_section('video')
        writer.add_section('api')
        writer.set('video', 'device', 'fbdev2')
        writer.set('api', 'token', '')

        self.dev = 'fbdev2'
        self.token = None

        with open(CONF_PATH, 'w') as f:
            writer.write(f)

    def override(self, args):
        if args.dev:
            self.dev = args.dev
        if args.token:
            self.token = args.token

class YTArgs:
    def __init__(self, argv):
        parser = ArgumentParser('Command line options for youterm')
        parser.add_argument('--url', dest='url', type=str, default=None,
                            help='Used to play youtube video at url and exit')
        parser.add_argument('--device', dest='dev', type=str, default=None,
                            help='Device to use with mplayer. Overrides option in configuration file')
        parser.add_argument('--token', dest='token', type=str, default=None,
                            help='Token for youtube api. Overrides option in configuration file')
        args = vars(parser.parse_args(argv))
        self.url = args['url']
        self.dev = args['dev']
        self.token = args['token']

