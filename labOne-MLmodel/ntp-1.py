import ntplib

from time import ctime

c = ntplib.NTPClient()
'''
       server 0.asia.pool.ntp.org
	   server 1.asia.pool.ntp.org
	   server 2.asia.pool.ntp.org
	   server 3.asia.pool.ntp.org
'''
response = c.request('pool.ntp.org')

print(ctime(response.tx_time))