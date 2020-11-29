import requests


resp = requests.get('https://www.google.com')
print(resp.status_code)
print(resp.text)