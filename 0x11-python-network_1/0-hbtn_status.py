#!/usr/bin/python3
"""Practice using requests module"""
from urllib.error import HTTPError, URLError
import urllib.request as curl
import urllib.parse as parser

def main():
    """Main function"""
    url = 'https://alx-intranet.hbtn.io/status'
    
    req = curl.Request(url)
    try:
        with curl.urlopen(req) as response:
            html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
    except HTTPError as e:
        print('HTTPError: ', e.code)
    except URLError as e:
        print ('URLError ', e.reason)

if __name__ == '__main__':
    main()
