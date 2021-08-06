#!/usr/bin/env python
# coding:utf-8
# Filename: answer-flask.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "It's alive!"

@app.route('/home')
def anotherhome():
    kwargs = {}
    kwargs["thing"] = request.args.get('thing')
    kwargs["height"] = request.args.get('height')
    kwargs["color"] = request.args.get('color')
    return render_template('home.html',**kwargs)

app.run(port=5000,debug=True)
