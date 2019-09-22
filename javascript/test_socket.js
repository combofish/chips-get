#!/usr/bin/env node
// coding:utf-8
// Filename: test_socket.js
'use strict'

var  net = require('net')

net.createServer((socket) => {
    socket.write('Hello World!\r\n')
    socket.end()
}).listen(1337)

console.log('Listen on port 1337!')

