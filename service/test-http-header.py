import requests

url = 'https://www.blognone.com'

response = requests.get(url)

headers = response.headers

html = response.text

with open('header.txt', 'w') as file:
    file.write(headers.__repr__())
    file.close()
