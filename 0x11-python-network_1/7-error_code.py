#!/usr/bin/python3
"""Practice using requests module"""
import requests
import sys


def main():
    """Main function"""
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    req = requests.post(url, data=email)

    print(req.text)


if __name__ == '__main__':
    main()
