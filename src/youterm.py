#!/usr/bin/python3
import curses
from curses import wrapper
from sys import exit, argv
from ytconfig import YTConfig, YTArgs
from ytplayer import YTPlayer
from ytquerry import YTQuerry

def main():
    if args.url:
        player.play_video(url=args.url)
        return 0
    
    if conf.token:
        yt = YTQuerry(conf.token)
    else:
        print('ERROR: No youtube api token provided')
        return 1
    wrapper(tui)

    return 0

def tui(stdscr):
    while(True):
        try:
            stdscr.clear()


            stdscr.refresh()
            stdscr.getkey()
        except KeyboardInterrupt:
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            return

if __name__ == '__main__':
    conf = YTConfig()
    args = YTArgs(argv[1:])
    conf.override(args)
    player = YTPlayer(conf.dev)
    exit(main())

