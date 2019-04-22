from urllib.request import urlopen as urlReq
from urllib.error import URLError
import json


class Request:

    def __init__(self, url):
        self.url = url

    def get_page_html(self):
        try:
            url_client = urlReq(self.url)
            page_html = url_client.read()
            url_client.close()
            return page_html
        except URLError as e:
            return 'HTTPError = ' + str(e)

