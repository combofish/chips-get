#!/usr/bin/env python
# coding:utf-8
# Filename: flask1.py

from flask import Flask

app = Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('./index-test.html')

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing

app.run(port=9999,debug=True)

