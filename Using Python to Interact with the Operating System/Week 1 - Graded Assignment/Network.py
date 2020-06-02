#!/usr/bin/env python3

import requests
import socket

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == '127.0.0.1':
                return True
        else:
                return False

def check_connectivity():
        request = requests.get('http://www.google.com')
        response =  request.status_code
        if response == 200:
                return True
        else:
                return False


# Follow the instructions
# request.status_code: According to documents, it is an object class called by request. It will return a status code like 200 or 404
