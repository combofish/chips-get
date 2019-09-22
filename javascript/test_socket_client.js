#!/usr/bin/env node
// coding:utf-8
// Filename: test_socket_client.js
'use strict'


var net = require('net')

var socket = net.connect({host: process.argv[2], port: 22})
socket.setEncoding('utf8')
socket.once('data',(chunk) => {
    console.log('SSH server version:%j', chunk.trim())
    console.log(chunk)
    socket.end();
})

