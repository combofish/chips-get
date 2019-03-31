#!/usr/bin/env node


const http = require('http'),
      fs  = require('fs'),
      path = require('path'),
      mime = require('mime-types'),
      chatServer = require('./lib/chat_server.js')
var cache = {}

function send404(response){
    response.writeHead(404,{'Content-Type':'text/plain'})
    response.write('Error: resource not found.')
    response.end()
}

function sendFile(res,filePath,fileContents){
    res.writeHead(
	200,{"Content-Type":mime.lookup(path.basename(filePath))}
    )
    res.end(fileContents)
}

function serveStatic(res, cache, absPath){
    if(cache[absPath]){
	sendFile(res,absPath,cache[absPath])
    }else{
	fs.exists(absPath,function(exists){
	    if(exists){
		fs.readFile(absPath,function(err,data){
		    if(err){
			send404(res)
		    }else{
			cache[absPath] = data
			sendFile(res,absPath,data)
		    }})
	    }else{
		send404(res)}})}
}

const server = http.createServer(function(req,res){
    var filePath = false;

    if(req.url == '/'){
	filePath = 'public/index.html'
    }else{
	filePath = 'public' + req.url
    }

    var absPath = './' + filePath
    serveStatic(res,cache,absPath)})

chatServer.listen(server)

server.listen(3000,function(){
    console.log("Server listening on post 3000.")})

