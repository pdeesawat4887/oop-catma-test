import requests
import threading


class Webservice:
    host_list = []
    num = 1
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.99'}

    def __init__(self, url, status=None, reason=None):
        self.url = url
        self.status = status
        self.reason = reason

    def checkStatusHTTPS(self, protocol):
        try:
            res_https = requests.get(protocol + self.url, headers=Webservice.headers)
            self.status = res_https.status_code
            self.reason = res_https.reason
            res_https.close()
        except Exception as ex:
            self.status = 'Could not connect to page.'
            self.reason = 'Could not connect to page.'

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
            temp_file.write(('{:^8}\t{:^24}\t{:^16}\t{:^24}\t{:^24}\n').format(no, url, protocol, status, reason))
            temp_file.close()


protocols = ['https://', 'http://']
obj = list()

Webservice.readURL('host.txt')
Webservice.writeReport('report.txt', '   NO   ', '         DOMAIN         ', '    PROTOCOL     ', '         STATUS         ',
                       '         REASON         ')
Webservice.writeReport('report.txt', '--------', '------------------------', '-----------------', '------------------------',
                       '------------------------')

for i in range(len(Webservice.host_list)):
    obj.append(Webservice(Webservice.host_list[i]))


def run():
    threading.Timer(10.0, run).start()

    for i in obj:
        for protocol in protocols:
            i.checkStatusHTTPS(protocol)
            p_protocol = 'HTTPS' if protocol == 'https://' else 'HTTP'
            Webservice.writeReport('report.txt', Webservice.num, i.url, p_protocol, i.status, i.reason)

    Webservice.num += 1
    Webservice.writeReport('report.txt', '--------', '------------------------', '-----------------',
                           '----------------',
                           '----------------')


run()
