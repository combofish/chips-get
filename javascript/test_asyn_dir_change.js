#!/usr/bin/env node
// coding:utf-8
// Filename: test_asyn_dir_change.js
'use strict'

var fs = require('fs'),
    writeStream = fs.createWriteStream('./log.txt',{
        'flags':'a',
        encoding:'utf8'
    }),
    counter = 0 

try{
    fs.readdir('./chatrooms/', (err,files) =>{
        console.log(files.length)
        
        files.forEach((name) => {
            fs.lstat('./chatrooms/' + name, (err, stats) => {
                if (!stats.isFile()) {return }

                fs.readFile('./chatrooms/' + name, 'utf8', (err, data) => {
                    if (err) throw err
                    var adjdata = data.replace(/combofish/g,'burningbird.net')
                    fs.writeFile('./chatrooms/new_' +  name, adjdata, (err) => {
                        if (err) throw err

                        writeStream.write('changed ' + name + '\n', 'utf8', (err) => {
                            if (err) throw err
                            console.log('finished ' + name)
                            counter++
                            //console.log(counter)
                            
                            if (counter >= (files.length - 2))
                                console.log('all done totally!')
                        })
                    })
                })  
            })
        })
        
        console.log('all done')
    })
}catch(err) {
    console.error(util.inspect(err))
}

