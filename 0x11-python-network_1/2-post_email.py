#!/usr/bin/python3
"""Send POST to adress with email attached"""
from urllib.error import HTTPError, URLError
import urllib.request as curl
import urllib.parse as parser
import sys


def main():
    """Main function"""
    url = sys.argv[1]
    email = parser.urlencode({'email': sys.argv[2]})
    email = email.encode('ascii')
    req = curl.Request(url)
    try:
        with curl.urlopen(req, email) as response:
            html = response.read()

        print(html.decode('utf-8'))
    except HTTPError as e:
        print('HTTPError: ', e.code)
    except URLError as e:
        print('URLError ', e.reason)


if __name__ == '__main__':
    main()
