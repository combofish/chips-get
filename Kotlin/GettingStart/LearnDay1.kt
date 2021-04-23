import java.lang.Exception
import java.math.BigInteger
import java.util.*

fun main(args: Array<String>) {



}


/**
{
//println(ollAdd(100000))
var res = 0
println(ollAdd3(100,res))
println(res)

}
fun ollAdd(n:Int):Int = if(n==1) 1 else n+ollAdd(n-1)
tailrec fun ollAdd2(n:Int,res:Int):Int = if (n ==1) 1 else ollAdd2(n-1,res+n)
tailrec fun ollAdd3(n:Int,res:Int):Int {
println(res+n)
if (n ==1) {
return 1
} else {
return ollAdd3(n-1,res+n)
}
}


/**

{
println(fact(5))
println(fact(3))
println(fact(10))
println(fact(100))
println(factBig(BigInteger("30")))

}

fun fact(n:Int):Int = if(n == 1) 1 else n*fact(n-1)
fun factBig(n:BigInteger):BigInteger = if (n==BigInteger.ONE) BigInteger.ONE else n*factBig(n- BigInteger.ONE)


/**
{
while (true) {
try {
var num = "1a"!!.toInt()
println(num)
} catch (e: Exception) {
println("err")
}
}

}


/**
{
println("please enter a number")
var num1Str = readLine()
//var num1 = num1Str?.toInt()
val num1 = num1Str!!.toInt()

println(num1)
}
}


/**
{
var a = "13"
var b = 13
println(b.toString())
println(a.toInt())
}

/**
{
println(getCircleArea(r = 3.9f))
}

fun getRectArea(l:Int,w:Int):Int{
return l*w
}

fun getCircleArea(PI:Float = 3.14f,r:Float):Float{
return PI * r * r
}

/**
{
var i = {a:Int,b:Int -> a+b}

var j:(Int,Int) -> Int = {x,y -> x+y}
println(i(2,3))
}

fun add(a: Int, b: Int): Int {
return a + b
}

fun add2(a: Int, b: Int): Int = a + b


/**
{
var map = TreeMap<String, String>()
map["l1"] = "good"
map["l2"] = "well"

println(map["l1"])
}


/**
{

var lists = listOf<String>("dog","egg","duck")
println(lists)

for (list in lists)
println(list)

for ((i,e) in lists.withIndex())
println("$i:$e")

}

/**
{
var nums = 1..100
println(nums)
print("$nums,")
var res = 0
for (num in nums)
res = res + num

println(res)
println(" ")
var nums3 = nums.reversed()
for (num in nums3)
print(num)

println()
println(nums3.count())
}

/**
{
println(gradeStudent(9))
println(gradeStudent(10))
println(gradeStudent(2))
}

fun gradeStudent(score: Int): String {
return when (score) {
10 -> "good"
9 -> "bad"
else -> "worse"
}
}

/**
{

var str1 = "张三"
var str2 = "李四"
println(str1 == str2)
println(str1.equals(str2))
println(str1.equals(str2, false))

println(face(99))
println(face(9))
println(heat("dog"))
println(heat(null))
}

fun heat(str:String?):String{
return "hot$str"
}
fun face(score: Int): String {
return if (score > 90) "Handsome" else "Ugly"
}


/**
{
println("Hello World!")
var i = 9999;
i = 999999999
var j = 99999999999999999;
var u:Byte = 88;
var s = "sji"
s = "ush"

val uw = "jsis"
//uw = "jdsi"
var a = 9
var b = 3
println("a+b= "+ plus(a,b))
println(sayHello("Larry"))
println(checkAge(90))
logLevel(9)
println(diaryGenerater("海河"))
}

fun diaryGenerater(placeName:String):String{
var template_use = """
我去${placeName}，我在${placeName}玩了好几天。
""".trimIndent()
return template_use
}
fun sayHello(name:String):String{
return "SayHello$name"
}

fun checkAge(age:Int):Boolean{
return age > 18
}

fun logLevel(logLevel1:Int){

}

fun plus(a:Int,b:Int):Int{
return a+b
}

fun sub(a:Int,b:Int):Int{
return a-b
}

fun mul(a:Int,b:Int):Int{
return a*b
}

fun div(a:Int,b:Int):Int{
return a/b
}
 */





