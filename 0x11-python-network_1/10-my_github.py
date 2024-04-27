#!/usr/bin/python3
"""Practice using requests module"""
import requests
import sys


def main():
    """Main function"""
    user = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url, auth=(user, token))
    data = response.json()
    try:
        print(data['id'])
    except KeyError:
        print("None")


if __name__ == '__main__':
    main()
