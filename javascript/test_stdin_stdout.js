#!/usr/bin/env node
// coding:utf-8
// Filename: test_stdin_stdout.js
'use strict'


process.stdin.resume()

process.stdin.on('data',(chunk) => {
    process.stdout.write('data: ' + chunk)
})

