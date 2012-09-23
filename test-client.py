#!/usr/local/bin/python3

import http.client
import sys
import codecs

#topost = sys.stdin.read()
#topost = open('../lua-lingrbot/test-show.txt').read()
topost = open('../lua-lingrbot/test-print-a.txt').read()

conn = http.client.HTTPConnection("localhost", 10888)
conn.set_debuglevel(2)

conn.request(method='POST',url='/cgi/index.cgi', body=topost)

response = conn.getresponse()

print(response.status)
print(response.getheader("Content-Type"))
print(response.getheader("Content-Length"))
utf8 = codecs.getdecoder('utf8')
s = utf8(response.read())
response.close()
conn.close()
print(s)

