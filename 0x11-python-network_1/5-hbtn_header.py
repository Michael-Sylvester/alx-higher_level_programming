#!/usr/bin/python3
"""Practice using requests module"""
import requests
import sys


def main():
    """Main function"""
    url = sys.argv[1]
    req = requests.post(url)

    print(req.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
