import httplib
import sys

def get_page_source(url):
    http_client = httplib.HTTP(url)

    http_client.putrequest("GET", "/")
    http_client.endheaders()
    errcode, errmessage, headers = http_client.getreply()
    f = http_client.getfile()
    print(f.read())

if __name__ == '__main__':
    url = sys.argv[1]
    get_page_source(url)
