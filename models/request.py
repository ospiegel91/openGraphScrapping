from urllib.request import urlopen as urlReq
from urllib.error import URLError
import json


class Request:

    def __init__(self, url):
        self.url = url

    def get_page_html(self):
        try:
            urlClient = urlReq(self.url)
            page_html = urlClient.read()
            urlClient.close()
            return page_html
        # status code
        except URLError as e:
            return 'HTTPError = ' + str(e)

