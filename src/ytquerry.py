from youtube_api import YoutubeDataApi

BASE_URL = 'https://www.youtube.com/watch?v={}'

class YTQuerry:
    def __init__(self, token):
        self.token = token
        self.api = YoutubeDataApi(token)

    def get_url(self, video_id):
        return BASE_URL.format(video_id)

    def search_videos(self, q, results=5):
        return self.api.search(q=q, max_results=results)
