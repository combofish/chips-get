// dup1 输出便准输入中出现次数大于1的行，前面是次数
package main

import ( "fmt"
	"os"
	"bufio"
)

func main () {
	counts := make(map[string]int)
	imput := bufio.NewScanner(os.Stdin)
	for imput.Scan() {
		counts[imput.Text()]++
	}

	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n , line)
		}
	}
}
