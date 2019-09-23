#!/usr/bin/env node
// coding:utf-8
// Filename: test_last_callback_functionality.js
'use strict'


var obj = function(){}

obj.prototype.doSomething = (arg1, arg2_) => {
    var arg2 = typeof(arg2_) === 'string' ? arg2_ : null

    console.log(arguments[arguments.length - 1])
    
    var callback_ = arguments[arguments.length - 1],
        callback = (typeof(callback_) == 'function' ? callback_ : null)

    console.log(callback)
    
    if(!arg2)
        return callback(new Error('second argument missing or not a string'))

    callback(arg1)
}

var test = new obj();
try{
    test.doSomething('test',3.55, (err,value) => {
        if(err) throw err

        console.log(value)
    })
}catch(err){
    console.log(err)
}
