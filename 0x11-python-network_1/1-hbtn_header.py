#!/usr/bin/python3
"""Display X-Request-Id from response"""
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
            headers = response.getheaders()

        for name, value in headers:
            if name == 'X-Request-Id':
                print(value)
    except HTTPError as e:
        print('HTTPError: ', e.code)
    except URLError as e:
        print ('URLError ', e.reason)

if __name__ == '__main__':
    main()
