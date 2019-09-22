#!/usr/bin/env node
// coding:utf-8
// Filename: test_socket_pipe_client.js
'use strict'


var  net = require('net')

net.createServer((socket) => {
    console.log('socket connect')

    socket.on('data',(data) => {
        console.log('"data" event',data)
    })
    socket.on('end',() =>{
        console.log('"end" event')
    })
    socket.on('close',() =>{
        console.log('"close event')
    })
    socket.on('error',(e) => {
        console.log('"error" event',e)
    })
    socket.pipe(socket)

}).listen(1337)

console.log('Listen on port 1337!')
