#!/usr/bin/python3
"""Practice using urllib module"""
from urllib.error import HTTPError, URLError
import urllib.request as curl
import urllib.parse as parser
import sys


def main():
    """Main function"""
    url = sys.argv[1]
    req = curl.Request(url)
    try:
        with curl.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('URLError ', e.reason)


if __name__ == '__main__':
    main()
