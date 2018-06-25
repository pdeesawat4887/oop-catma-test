import httplib
import requests
import threading


class Webservice:
    host_list = []
    num = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.99'}
    HTTP = 'HTTP'
    HTTPS = 'HTTPS'

    def __init__(self, url, status=None, reason=None):
        self.url = url
        self.status = status
        self.reason = reason

    def createConnection(self):
        response = requests.get('https://' + self.url, headers=Webservice.headers)
        # conn = httplib.HTTPConnection(self.url)
        # conn.request('HEAD', '/')
        # temp_res = conn.getresponse()
        self.status = response.status_code
        self.reason = response.reason
        response.close()

    # def checkStatusHTTP(self):
    #     res_http = requests.get('http://' + self.url, headers=Webservice.headers)
    #     self.status = res_http.status_code
    #     self.reason = res_http.reason
    #     res_http.close()

    def checkStatusHTTPS(self):
        try:
            res_https = requests.get('https://' + self.url, headers=Webservice.headers)
            self.status = res_https.status_code
            self.reason = res_https.reason
            res_https.close()
        except Exception as ex:
            self.error_here()
            self.status = 'ERROR'
            self.reason = 'ERROR'

    # @staticmethod
    def error_here(self):
        print('Could not connect to page.')

    # def print_url(self):
    #     return 'You typing https://{}'.format(self.url)
    #
    # def print_url_status(self):
    #     return 'Your testing result is {}'.format(self.status)
    #
    # def print_url_reason(self):
    #     return 'Your testing mean {}'.format(self.reason)

    @classmethod
    def readURL(cls, file):
        with open(file, 'r') as temp_file:
            text = temp_file.read()
            cls.host_list = text.split()
            temp_file.close()
            return cls.host_list

    @classmethod
    def writeReport(cls, file, no, url, protocol, status, reason):
        with open(file, 'a') as temp_file:
            temp_file.write(('{:^8}\t{:^24}\t{:^16}\t{:^16}\t{:^16}\n').format(no, url, protocol, status, reason))
            temp_file.close()
            print 'Write file already'


# url_test_1 = Webservice(raw_input('Enter your url testing: '))
# url_test_1.createConnection()
#
# print url_test_1.print_url()
# print url_test_1.print_url_status()
# print url_test_1.print_url_reason()

Webservice.readURL('host.txt')
Webservice.writeReport('report.txt', '   NO   ', '         DOMAIN         ', '    PROTOCOL     ', '     STATUS     ',
                       '     REASON     ')
Webservice.writeReport('report.txt', '--------', '------------------------', '-----------------', '----------------',
                       '----------------')

# Webservice.readURL(raw_input('Enter text file that contain list of host: '))

obj = list()
for i in range(len(Webservice.host_list)):
    obj.append(Webservice(Webservice.host_list[i]))


def run():
    threading.Timer(10.0, run).start()

    for i in obj:
        # i.createConnection()
        # i.checkStatusHTTP()
        # Webservice.writeReport('report.txt', Webservice.num, i.url,Webservice.HTTP, i.status, i.reason)
        i.checkStatusHTTPS()
        Webservice.writeReport('report.txt', Webservice.num, i.url, Webservice.HTTPS, i.status, i.reason)
        # print Webservice.num, i.url, i.status, i.reason

    Webservice.num += 1


run()
