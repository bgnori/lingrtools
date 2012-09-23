#!/usr/local/bin/python3

import http.server
import os
import sys

h = http.server.CGIHTTPRequestHandler
#h.cgi_directories = [os.path.join(os.getcwd(),"cgi")]
h.cgi_directories = ["/cgi"]
sv = http.server.HTTPServer(("localhost", 10888), h)
sv.serve_forever()

