from models.request import Request
from models.bSoup import BSoup
from models.openGraph import OpenGraph
from models.ResponseBuilder import ResponseBuilder
import json
import sys


def main():
    try:
        URL = sys.argv[1]
    except IndexError:
        URL = 'http://ogp.me/'

    user_request = Request(URL)
    page_html = user_request.get_page_html()
    if page_html[:9] == 'HTTPError':
        res = json.dumps({
            'STATUS': 'ERROR',
            'MSG': "bad url request error, page not found",
            "CATEGORIES": page_html,
            'CODE': "404"
        })
        print(res)
        return res

    request_bsoup = BSoup(page_html)
    page_bsoup = request_bsoup.return_bSoup_object_from_page_html()

    og_obj = OpenGraph(page_bsoup)
    res = ResponseBuilder(og_obj).get_response_object_in_json()

    print(res)
    return res


if __name__ == '__main__':
    main()

