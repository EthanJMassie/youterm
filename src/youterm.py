#!/usr/bin/python3
import curses
from curses import wrapper
from sys import exit, argv
from ytconfig import YTConfig, YTArgs
from ytplayer import YTPlayer
from ytquerry import YTQuerry


def tui(stdscr):
    '''
        main function for curses tui
    '''
    while(True):
        try:
            stdscr.clear()


            stdscr.refresh()
            stdscr.getkey()
        except KeyboardInterrupt:
            clean(stdscr)
            return


def clean(stdscr):
    '''
        clean up the curses window stdscr
    '''
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()


if __name__ == '__main__':
    conf = YTConfig()
    args = YTArgs(argv[1:])
    conf.override(args)
    player = YTPlayer(conf.dev)

    if args.url:
        player.play_video(url=args.url)
        exit(0)
    
    if conf.token:
        yt = YTQuerry(conf.token)
    else:
        print('ERROR: No youtube api token provided')
        exit(1)
    
    wrapper(tui)

