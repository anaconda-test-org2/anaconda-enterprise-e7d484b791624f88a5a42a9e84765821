#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
from argparse import ArgumentParser
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus

class HelloHandler(BaseHTTPRequestHandler):
# path="scsc/scsxc/cs"
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        #print(self.wfile)
        #self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        #self.wfile.write(b"<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        #self.wfile.write(bytes(self.path , "utf-8")
        #self.wfile.write(b"</body></html>")
        #self.wfile.close()
        dirlist = os.listdir('~/var/run/secrets/')  
        self.wfile.write(b""+json.dumps(dirlist))     
        return
                         
        


def runserver(address, port):
    server_address = (address, int(port))
    httpd = HTTPServer(server_address, HelloHandler)
    try:
        print("Server available at {}:{}".format(address, port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server")
        httpd.socket.close()


# Arg parser for the anaconda-project http options
parser = ArgumentParser(prog="Hello Anaconda Enterprise", description="Minimal Anaconda Enteprise deployable example")
parser.add_argument('--anaconda-project-host', action='append', help='Hostname to allow in requests')
parser.add_argument('--anaconda-project-no-browser', action='store_true', default=False, help='Disable opening in a browser')
parser.add_argument('--anaconda-project-use-xheaders', action='store_true', default=False, help='Trust X-headers from reverse proxy')
parser.add_argument('--anaconda-project-url-prefix', action='store', default='', help='Prefix in front of urls')
parser.add_argument('--anaconda-project-port', action='store', default='8484', help='Port to listen on')
parser.add_argument('--anaconda-project-iframe-hosts', action='append', help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
parser.add_argument('--anaconda-project-address', action='store', default='0.0.0.0', help='IP address the application should listen on.')


if __name__ == '__main__':
    # This app accepts all anaconda-project http options, but ignores most of them.
    args = parser.parse_args(sys.argv[1:])
    runserver(address=args.anaconda_project_address, port=args.anaconda_project_port)