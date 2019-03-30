#!/usr/bin/python3
import os
import sys
import subprocess
import shlex
import argparse
import ytconfig
from subprocess import PIPE

def main():
    if args.url:
        play_video(url=args.url, device=conf.dev)
        sys.exit(0)
    


def play_video(url, device):
    ydl_args = shlex.split('youtube-dl -q -o- {}'.format(url))
    mpl_args = shlex.split('mplayer -vo {} -'.format(device))
    ydl_proc = subprocess.Popen(args=ydl_args, stdout=PIPE)
    mpl_proc = subprocess.Popen(args=mpl_args, stdout=None, stderr=None, stdin=ydl_proc.stdout)
    mpl_proc.wait()

if __name__ == '__main__':
    conf = ytconfig.YTConfig()
    args = ytconfig.YTArgs(sys.argv)
    conf.override(args)
    main()
