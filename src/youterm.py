#!/usr/bin/python3
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

    results = yt.search_videos('William Osman')

    for result in results:
        print(yt.get_url(result['video_id']))

    return 0

    while True:
        try:
            pass
        except KeyboardInterrupt:
            return 0

    return 0

if __name__ == '__main__':
    conf = YTConfig()
    args = YTArgs(argv[1:])
    conf.override(args)
    player = YTPlayer(conf.dev)
    exit(main())

