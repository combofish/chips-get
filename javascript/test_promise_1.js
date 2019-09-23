#!/usr/bin/env node
// coding:utf-8
// Filename: test_promise_1.js
'use strict'


new Promise((resolve, reject) =>{
    resolve(2)
}).then((data) =>{
    data++
    console.log('data: ',data)
    return 1
}).then((data) => {
    data++
    return data
}).then((data) =>{
    console.log("last : " + data)
})

console.log(1)
