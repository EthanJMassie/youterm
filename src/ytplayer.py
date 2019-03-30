import subprocess
import shlex
from subprocess import PIPE

class YTPlayer:
    def __init__(self, dev):
        self.dev = dev
    
    def play_video(self, url):
        '''
            Play youtube video at url
        '''
        ydl_args = shlex.split('youtube-dl -q -o- {}'.format(url))
        mpl_args = shlex.split('mplayer -really-quiet -vo {} -'.format(self.dev))
        # send output of ydl_proc to PIPE and use that as stdin for mpl_proc
        ydl_proc = subprocess.Popen(args=ydl_args, stdout=PIPE)
        mpl_proc = subprocess.Popen(args=mpl_args, stdout=None, stderr=None, stdin=ydl_proc.stdout)
        try:
            mpl_proc.wait()
        except KeyboardInterrupt:
            # clean up if user interupts process
            mpl_proc.kill()
        finally:
            # ensure the ydl_proc is dead
            ydl_proc.kill()