// dup2 打印输出中多次出现的行的个数和文本
// 它从 stdin 或指定的文件列表读取
package main

import (
	"bufio"
	"os"
	"fmt"
)

func main () {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	}else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2:%v\n", err)
				continue
			}
			countLines(f, counts)
			f.Close()
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

func countLines (f *os.File, counts map[string]int){
	input := bufio.NewScanner(f)
	for input.Scan() {
		counts[input.Text()]++
	}
	// 忽略 input.Err() 中可能出现的错误
}
