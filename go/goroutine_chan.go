// Filename: go.org[*Org Src go.org[ go ]*]
// coding:utf-8
// 使用通道进行通信
package main

import (
        "fmt"
        "time"
)

func main () {
        c := make(chan string)
        go slowFunc(c)

        msg := <-c
        fmt.Println(msg)
}

// 
func slowFunc (c chan string) {
        time.Sleep(time.Second * 2)
        c <- "slowFunc() finished"
}

