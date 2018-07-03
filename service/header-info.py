# import httplib
import requests
# try:
url = 'http://www.squid-cache.org/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.99'}
response = requests.get(url, headers=headers)
response.json()
print response.status_code
print response.headers
# print response.encoding
print response.request
# print response.text
    # h = httplib.HTTPConnection(url)
    # h.connect()
    # h.request("GET", "/")  # Could also use "HEAD" instead of "GET".
    # res = h.getresponse()
    # print res.status, res.reason
    # if res.status == 200 or res.status == 302:  # Specify codes here.
    #     print("Page Found!")
# except Exception as ex:
#     print "Could not connect to page."
#     print

