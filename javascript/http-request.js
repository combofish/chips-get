#!/usr/bin/env node

const https = require('https'),
 fs = require('fs')

var opt,req

function start(){
 opt = {
     hostname:'www.baidu.com',
     port:443,
     path:'/',
     method:'GET',
     agent:false,
 }

 req = https.request(opt, function(res){
     res.setEncoding('utf8')
     var body = ""

     res.on('data',function(chunk){
         body+=chunk
     })

     res.on('end',function(){
         console.log(body)
     })
 })


req.setTimeout(5000,function(){
    req.abort()
})

req.on('error',function(er){
    if(err.code == 'ECONNRESET'){
        console.log('time out.')
    }else{
        console.log('request error.')
    }
})

    req.end()
}

start()







