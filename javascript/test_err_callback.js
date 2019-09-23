#!/usr/bin/env node
// coding:utf-8
// Filename: test_err_callback.js
'use strict'


var A = {method:(cb) => {
    try{
        cb("this is A")
    }catch(e){
        console.log("catch error in A",e,this)
        throw e 
    }
}},
    B = {method:(res) => {
        console.log("This is B", res,this)
        throw new Error("try cause error in B")
    }}

try {
    A.method(B.method)
}catch (e){
    console.log("catch error",e)
}
