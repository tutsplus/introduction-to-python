import ntplib
from time import ctime

def get_current_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print 'Current time is', ctime(response.tx_time)

if __name__ == '__main__':
    get_current_time()
