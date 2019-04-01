var app = function(){
    this.size = 30
        this.getSize = function(){
            console.log(this.size)
        }
        this.show = function(){
            return this.light
        }
}

var weixin = new app()
weixin.getSize()
console.log(weixin.__proto__)
console.log(weixin.constructor)

app.prototype.use =  300
console.log(weixin.use)
console.log(weixin.prototype) //undefined

app.prototype.getUse = function(){
    return this.use
}

console.log(weixin.getUse)
console.log(weixin.getUse()) //300

var weixin2 = new app()
console.log(weixin2.getUse()) //300

weixin2.use = 356
console.log(weixin.use) //300
console.log(weixin2.use) //356

console.log(weixin.getUse()) //300
console.log(weixin2.getUse()) //356

//weixin2.prototype.use = 789
app.prototype.use = 999
console.log(weixin.getUse()) //999
console.log(weixin2.getUse()) //356

// weixin2.prototype.putStr = function(){
app.prototype.putStr = function(){
    console.log('hello world')
}

weixin2.putStr()

console.log(weixin2.__proto__)

app.prototype = {
    weight:3,
    getWeight:function(){
        console.log(this.weight)
    },
}

console.log(weixin2.__proto__)
console.log(weixin2.prototype) //undifined
// weixin2.getWeight() //error

app.prototype.useObj = {
    color:255,
    changeColor:function(a){
        this.color = a
    },
}

// weixin2.useObj.changeColor() //undefined
console.log(weixin.__proto__)
console.log(weixin.useObj) //undefined
// console.log(weixin.useObj.color)



