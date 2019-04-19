#!/usr/bin/python
#-*- coding: utf-8 -*-

import argparse
import commands
from flask import Flask, jsonify,request
import sys
from flask import redirect
app = Flask(__name__)

@app.route('/name2',methods=['POST'])
def name2_check():
        if request.method=='POST':
                num=1;
		fib0=0;
		fib1=1;
                try:
                        n=int(request.form['firstname'])
                except:
                        return "Input error"
                for i in range(1,n):
			num=fib1+fib0
			fib0=fib1
			fib1=num
                return "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><b>%d</b><form action=\"/name2\" method=\"post\"><p>Input number: <input type=\"text\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"% num


@app.route('/', methods=['GET'])
def hello_test():
        return "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Post</title></head><body><form action=\"/name2\" method=\"post\"><p>Input number: <input type=\"text\" name=\"firstname\"></p><input type=\"submit\" value=\"submit\"></form></body></html>"

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('--listen-port',  type=str, required=True, help='REST service listen port')
        args = parser.parse_args()
        listen_port = args.listen_port
    except Exception, e:
        print('Error: %s' % str(e))

    ipaddr=commands.getoutput("hostname -I").split()[0]
    print "Starting the service with ip_addr="+ipaddr
    app.run(debug=False,host=ipaddr,port=int(listen_port))
