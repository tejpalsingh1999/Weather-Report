import requests

try:
    r = requests.get('http://udacity.com')
    print(r.status_code)
    print(r)
except requests.exceptions.ConnectionError:
    print('Could not connect to server')
