fun main() {
    println(Week.星期一)
    println(Week.星期一.ordinal)

}

enum class Week{
    星期一,星期二
}

/**
 {
     var apple1 = Apple()
 println(apple1.isGrowOnTree())
 println(apple1.grow())

 var apple2 = Apple()
 var box = listOf<Tree>(apple1,apple2)
 for (a in box)
 println(a.grow())
 }

 interface Food {
     fun isGrowOnTree(): Boolean
 }

 abstract class Tree(){
     abstract fun grow() : String
 }

 class Apple : Tree(),Food {
     override fun grow() = "Growing"
 override fun isGrowOnTree(): Boolean = true
 }

/**
 {
     var larry = Man("Larry")
 var lili = Woman("Lili")
 println(larry.eat())
 println(lili.eat())
 }

 abstract class Human(var name:String){
     abstract fun eat():String
 }

 class Man(name:String):Human(name){
     override fun eat():String = "猪肉"
 }

 class Woman(name:String):Human(name){
     override fun eat():String = "青菜"
 }


/**
 {
     var son1 = Son()
 println(son1.characher)
 println(son1.speak())
 }

 open class Father{
     var characher:String = "好动"
 open fun speak():String = "我说我$characher。"
 }

 class Son:Father(){
     override fun speak(): String {
     return "儿子:${super.speak()}"
 }
 }

/**
 {
     var washMachine = Machine("Little Mi", 20)
 println(washMachine.doJob())
 println(washMachine.runIn220())

 }

 class Machine(var name: String, var size: Int) {
     var runInStrongElectric = true
 fun doJob(): String = "${name} can do ${size.toString()} 工作量。${runInStrongElectric}"
 fun runIn220(): Boolean = !runInStrongElectric
 private fun setLogo(logo:String) {
     name = logo
 }
 }




/**
 {
     var apple = Food("Apple","Red")
 println(apple.cut())
 }

 class Food(var name:String,var color:String){
     fun cut():String = "切$name"
 }


/**
 {
     var car1 = Car(12,"BWM")
 println(car1.name)
 }

 class Car(var l:Int,var name:String)


/**
 {
     var rect1 = Rect(20,30)
 println(rect1.height)
 println(rect1.width)
 }

 class Rect(var height:Int,var width:Int)
 */
