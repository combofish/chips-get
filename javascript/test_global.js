// coding:utf-8
// Filename: test_global.js
'use strict'


var globalValue
exports.setGlobal = (val) => {
    globalValue = val
}

exports.returnGlobal = () => {
    console.log(global)
    return globalValue
}
