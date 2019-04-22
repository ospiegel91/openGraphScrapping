from models.request import Request
from models.bSoup import BSoup
from models.openGraph import OpenGraph
from models.ResponseBuilder import ResponseBuilder
import json
import sys


def main():
    try:
        url = sys.argv[1]
    except IndexError:
        url = 'http://ogp.me/'

    page_html = Request(url).get_page_html()
    if page_html[:9] == 'HTTPError':
        res = json.dumps({
            'STATUS': 'ERROR',
            'MSG': "bad url request error, page not found",
            "CATEGORIES": page_html,
            'CODE': "404"
        })
        print(res)
        return res

    page_bsoup = BSoup(page_html).return_bSoup_object_from_page_html()
    res = ResponseBuilder(OpenGraph(page_bsoup)).get_response_object_in_json()

    if res == '{}':
        res = json.dumps({
            'STATUS': 'ERROR',
            'MSG': "No open graph meta was found for the given url",
            "CATEGORIES": "no open graph meta tags",
            'CODE': "404"
        })
    print(res)
    return res


if __name__ == '__main__':
    main()

