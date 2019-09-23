#!/usr/bin/env node
// coding:utf-8
// Filename: test_asyn_exec.js
'use strict'

var fs = require('fs')

try{
    fs.readFile('./apples2.txt','utf8', (err,data) => {
        if (err) throw err

        var adjdata = data.replace(/[A|a]pple/g,'orange')
        fs.writeFile('./oranges.txt', adjdata, (err) => {
            if (err) throw err 
        })
    })
}catch(err){
    console.error(err)
}

