#!/usr/bin/env python
# coding:utf-8
# Filename: flask1.py

from flask import Flask, render_template

app = Flask(__name__,static_folder='.',static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('./index-test.html')

@app.route('/echo/<thing>/<place>')
def echo(thing,place):
    return render_template('flask2.html',thing=thing,place=place)

app.run(port=9999,debug=True)

