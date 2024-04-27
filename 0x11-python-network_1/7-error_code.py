#!/usr/bin/python3
"""Practice using requests module"""
import requests
import sys


def main():
    """Main function"""
    url = sys.argv[1]
    req = requests.get(url)

    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)


if __name__ == '__main__':
    main()
