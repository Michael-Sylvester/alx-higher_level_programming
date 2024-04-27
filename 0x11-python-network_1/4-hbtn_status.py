#!/usr/bin/python3
"""Practice using requests module"""


import requests
def main():
    """Main function"""
    req = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.content.decode('utf-8')))

if __name__ == '__main__':
    main()