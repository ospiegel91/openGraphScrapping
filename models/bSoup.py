from bs4 import BeautifulSoup as bSoup


class BSoup:

    def __init__(self, page_html):
        self.page_html = page_html

    def return_bSoup_object_from_page_html(self):
        return bSoup(self.page_html, 'html.parser')