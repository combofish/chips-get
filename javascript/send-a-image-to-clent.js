#!/usr/bin/env node

const http = require('http'),
      fs = require('fs')
http.createServer(function(req,res){
 res.writeHead(200, {'Content-Type':'image/jpg'})
 fs.createReadStream('./new-cam.jpg').pipe(res)
}).listen(3000)
console.log('Server is running at http://localhost:3000/')
