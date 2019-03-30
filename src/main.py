#!/usr/bin/python3
import os
import sys
import subprocess
import shlex
from subprocess import PIPE


def main():
    play_video(url='https://www.youtube.com/watch?v=waQ6IrUksBw')


def play_video(url, device='fbdev2'):
    ydl_args = shlex.split('youtube-dl -q -o- {}'.format(url))
    mpl_args = shlex.split('mplayer -vo {} -'.format(device))
    ydl_proc = subprocess.Popen(args=ydl_args, stdout=PIPE)
    mpl_proc = subprocess.Popen(args=mpl_args, stdin=ydl_proc.stdout)
    mpl_proc.wait()

if __name__ == '__main__':
    main()
