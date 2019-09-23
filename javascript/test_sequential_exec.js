#!/usr/bin/env node
// coding:utf-8
// Filename: test_sequential_exec.js
'use strict'


var fs = require('fs')

try{
    var data = fs.readFileSync('./apples.txt','utf8')
    console.log(data)
    var adjdata = data.replace(/[A|a]pple/g,'orange')

    fs.writeFileSync('./oranges.txt', adjdata)
}catch (err){
    console.error(err)
}
