// 带索引输出命令行参数
package main

import (
	"fmt"
	"os"
)

func main() {

	for i := 0; i < len(os.Args); i++{
		fmt.Println(i, os.Args[i])
	}
}
