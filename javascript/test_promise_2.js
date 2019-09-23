#!/usr/bin/env node
// coding:utf-8
// Filename: test_promise_2.js
'use strict'


new Promise((resolve, reject) => {
    var n = 3.14
    resolve(n)
    //    reject(new error())
}).then((n) => {
    return (n * n)
},(n) =>{
    return (n * n * n)
}).then(console.log,console.err)



