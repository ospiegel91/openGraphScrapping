import re

class OpenGraph:

    def __init__(self, page_bSoup):
        self.page_bSoup = page_bSoup

    def get_ogProp(self, prop):
        try:
            return self.page_bSoup.find("meta",  property="og:"+prop)["content"]
        except:
            return "could not find specified og property! Are you sure is exists for the desired web page?"

    def find_all_og_props(self):
        return self.page_bSoup.find_all("meta", property=re.compile("^og:"))

    def find_all_og_props_by_extension(self, extension):
        return self.page_bSoup.find_all("meta", property=re.compile("^og:"+extension))