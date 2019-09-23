#!/usr/bin/env node
// coding:utf-8
// Filename: test_promise_3.js
'use strict'


var p1 = new Promise((resolve, reject) => {
    resolve(['successful', 'a','three'])
})

p1.then(console.log,console.error)
console.log(typeof(p1))
