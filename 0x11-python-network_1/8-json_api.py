#!/usr/bin/python3
"""Practice using requests module"""
import requests
import sys


def main():
    """Main function"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    req = requests.post(url, data=data)

    try:
        jdata = req.json()
        if jdata and jdata is not None:
            print("[{}] {}".format(jdata.get("id"), jdata.get("name")))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
