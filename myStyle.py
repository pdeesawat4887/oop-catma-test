import httplib
import threading
from datetime import datetime

class testing(object):
    def __init__(self, filename):
        self.filename = filename
        self.words = self.file_to_text()
    def file_to_text(self):
        with open(self.filename, "r") as file_opened:
            text = file_opened.read()
            words = text.split()
            return words
    def createFile(self, filename):
        self.filename = filename
        f = open(filename, "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
        f.close()


alice = testing('requestTest.txt').file_to_text()
# print alice

class httpTest(object):
    def openConnection(self, host):
        self.host = host
        self.conn = httplib.HTTPConnection(host)
        self.conn.request('HEAD', '/')
        self.response = self.conn.getresponse()
        self.conn.close()
        return host, self.response.status, self.response.reason
        # self.url = 'https://{}'.format(host)
        # print 'Trying: {0}'.format(self.url)
        # print '    Got: ', self.response.status, self.response.reason

    def writeFile(self, host, status, reason):
        with open('result.txt', 'a') as file:
            self.url = 'https://{}'.format(host)
            file.write('Trying: {0}'.format(self.url)+'\n')
            file.write('Got: ' + str(status)+' '+ str(reason)+'\n')
            file.write(str(datetime.now())+'\n')
            file.write("\n")
            file.close()


def main():
    for website in alice:
        bob = httpTest().openConnection(website)
        jully = httpTest().writeFile(bob[0], bob[1], bob[2])
        threading.Timer(10, main).start()
main()
    # bob.writeFile(bo)

# jack = testing('database.txt').createFile()