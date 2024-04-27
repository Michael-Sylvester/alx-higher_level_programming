#!/usr/bin/python3
"""Practice using requests module"""
import requests

req = requests.get('http://michaelsylvester.tech')

print('Code: ', req.status_code)
print(len(req.content))



'''
data = {'name':'Michael', 'age':56} #if you want to send data in the query
r = requests.get('http://michaelsylvester.tech', params=data)
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')
# the information you can get includes
r.status_code
r.text #body of response
r.headers
r.options
r.reasons
r.cookies
#Custom headers
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
'''
if __name__ != "__main__":
    pass