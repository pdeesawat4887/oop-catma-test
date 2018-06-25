import os

def check_ping():
    hostname = "8.8.8.8"
    response = os.system("ping -c 1 -i 0.1 " + hostname)
    # and then check the response...
    # if response == 0:
    #     pingstatus = "Network Active"
    # else:
    #     pingstatus = "Network Error"
    #
    # return pingstatus
    print response

# check_ping()

import socket

def translate():
    hostname = 'www.github.com'
    resolve_ex = socket.gethostbyname_ex(hostname)
    resolve = socket.gethostbyname(hostname)
    print 'EX', resolve_ex
    print 'host', resolve
    print socket.getfqdn(hostname)
    print socket.gethostbyaddr(hostname)

# translate()


def ping_ipadd(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        ping_result = os.system("ping -c 1 -i 0.1 " + ip_address)
        print ping_result
        if ping_result == 0:
            ping_status = 'Active'
        else:
            ping_status = 'Check server first'
    except Exception as ex:
        ping_status = 'Cannot ping to destination'
    return ping_status

print ping_ipadd('https://google.com')




