# coding=utf-8
__author__ = 'Marc Solé Farré at Lleida'

#!/usr/bin/python

import sys

import requests

from client.Interpreter import Feedback

# example
# put in config file
server = "127.0.0.1:8000"
connection_error = "-1"

name = 'test'
module = ''
plugin = 'ls'
instruction = '-l'
instruction_value = '-a'
state = '1'

payload = {'name': name, 'plugin': plugin,
           'module': module, 'instruction': instruction,
           'instruction_value': instruction_value, 'state': state}
try:

    r = requests.post("http://"+server+"/client/job/hello/", data=payload)
    callback = r.text
except:
    # if not response
    callback = connection_error

my_file = open('callback.html', 'w')
Feedback.do_feedback(callback)

my_file.write(callback)
sys.exit(sys.argv[2])
