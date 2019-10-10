// Filename: go.org[*Org Src go.org[ go ]*]
// coding:utf-8
// 模拟阻塞的代码
package main

import (
	"fmt"
	"time"
)

func main () {
	slowFunc()
	fmt.Println("I'm not shown until slowFunc() completes.")
}

// 
func slowFunc () {
	fmt.Println("Sleepper() start")
	time.Sleep(time.Second)
	fmt.Println("Sleepper() finished")
}

