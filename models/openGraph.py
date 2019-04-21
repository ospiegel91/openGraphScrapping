import re


class OpenGraph:

    def __init__(self, page_bSoup):
        self.page_bSoup = page_bSoup

    def find_all_og_props(self):
        return self.page_bSoup.find_all("meta", property=re.compile("^og:"))

    def find_all_og_props_by_extension(self, extension):
        return self.page_bSoup.find_all("meta", property=re.compile("^og:"+extension))