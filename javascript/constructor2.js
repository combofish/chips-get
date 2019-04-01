function app(){
    var size = 40
        function show(){
            console.log('this.size:' +this.size)
        }
        function setSize(a){
            this.size = a
        }
    this.thisSize = 600
}

var weixin = new app()
console.log(weixin) // app {thisSize}
console.log(weixin.__proto__) // app{}
console.log(weixin.constructor) //{Function: app}

// weixin.show() //error not a function.
// app.show()  //error not a function.

console.log(weixin.prototype) //undefined
console.log(weixin.constructor)  // app{}
console.log(weixin.size) //undefined
//weixin.show()
console.log(weixin.thisSize) // 600

app.prototype.comp = 991
console.log(weixin) //app {thisSize: 600}
console.log(weixin.__proto__)  // app { comp: 991 }
console.log(weixin.comp) // 991
console.log(weixin.prototype) // undefined
console.log(app.prototype) // app { comp: 991 }
// next test

var app2 = {
    size:20,
    getSize:function(){
        console.log(this.size)
    },
}

//var weixin2 = new app2()
var weixin3 = Object.create(app2)
console.log(weixin3.size) // 20
console.log(weixin3.__proto__) // { size,getsize}
console.log(weixin3.constructor) // [function]
weixin3.getSize() //20

//weixin3.prototype = {
var ext = {
    light:300,
    showSize:function(){
        return this.size
    },
}

//console.log(weixin3.__proto__)
//console.log(weixin3.light)

weixin3.__proto__ = ext
console.log(weixin3.light) // 300
console.log(weixin3.__proto__) // { light,showsize }
console.log(weixin3.size) //undefined
console.log(app.prototype) // app { comp: 991}
