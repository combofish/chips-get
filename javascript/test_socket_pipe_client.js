#!/usr/bin/env node
// coding:utf-8
// Filename: test_socket_pipe_client.js
'use strict'


var net = require('net'),
    host = process.argv[2],
    port = Number(process.argv[3])

var socket = net.connect(port,host)

socket.on('connect',() => {
    process.stdin.pipe(socket)
    socket.pipe(process.stdout)
    process.stdin.resume()
    //    socket.write('haha')
})
socket.on('end',() =>{
    process.stdin.pause()
})
