#!/usr/bin/python3
"""Practice using urllib module"""
from urllib.error import HTTPError, URLError
import urllib.request as curl
import urllib.parse as parser

def main():
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

    data = parser.urlencode(values)
    send_data = data.encode('ascii')
    req = curl.Request(url + '?' + data)
    try:
        with curl.urlopen(req) as response:
            print(response.read())
    except HTTPError as e:
        print('HTTPError: ', e.code)
    except URLError as e:
        print ('URLError ', e.reason)

if __name__ == '__main__':
    main()
