#!/usr/bin/env node
// coding:utf-8
// Filename: test_promise_4_dir_change.js
'use strict'

const fsp = require('fs').promises

fsp.readFile('./apples.txt').then((data) => {
    console.log(data)
},e => {
    console.log('err: \n' + e.stack)
})
