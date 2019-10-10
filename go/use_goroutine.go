// Filename: go.org[*Org Src go.org[ go ]*]
// author: combofish
// coding:utf-8
// 使用goroutine
package main

import (
	"fmt"
	"time"
)

func main () {
	go slowFunc()
	fmt.Println("I'm not shown straightaway!")
}

// 
func slowFunc () {
	fmt.Println("Sleeper() started")
	time.Sleep(time.Second)
	fmt.Println("Sleeper() finished")
}
