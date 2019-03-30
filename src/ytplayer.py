import subprocess
import shlex
from subprocess import PIPE

class YTPlayer:
    def __init__(self, dev):
        self.dev = dev
    
    def play_video(self, url):
        ydl_args = shlex.split('youtube-dl -q -o- {}'.format(url))
        mpl_args = shlex.split('mplayer -really-quiet -vo {} -'.format(self.dev))
        ydl_proc = subprocess.Popen(args=ydl_args, stdout=PIPE)
        mpl_proc = subprocess.Popen(args=mpl_args, stdout=None, stderr=None, stdin=ydl_proc.stdout)
        mpl_proc.wait()