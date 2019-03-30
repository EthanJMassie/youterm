#!/usr/bin/python3
from sys import exit, argv
from ytconfig import YTConfig, YTArgs
from ytplayer import YTPlayer

def main():
    if args.url:
        player.play_video(url=args.url)
        return 0

    while True:
        pass

    return 0

if __name__ == '__main__':
    conf = YTConfig()
    args = YTArgs(argv[1:])
    conf.override(args)
    player = YTPlayer(conf.dev)
    exit(main())
