var myConstructor = function(){
    this.number = 5
}

newObject = new myConstructor()
console.log(newObject.number)

var myObj = {
    myString:"hello world"
}

var myPrototype = {
    meaningOfLife:42,
    myFunc:function(){
        return this.myString.toLowerCase()
    }
}

myObj.__proto__ = myPrototype
console.log(myObj.myFunc())
console.log(myObj.meaningOfLife) //42

myPrototype.__proto__ = {
    myBoolean:true
}

console.log(myObj.myBoolean)

myPrototype.meaningOfLife = 43
console.log(myObj.meaningOfLife) //43

myObj.meaningOfLife = 44
console.log(myPrototype.meaningOfLife) //43
console.log(myObj.meaningOfLife) //44


var myobj = Object.create(myPrototype)
console.log(myObj.meaningOfLife)  //44
console.log(myPrototype.meaningOfLife) //43

console.log(myObj)
