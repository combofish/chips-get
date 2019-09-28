//fetchall 并法获取URL 并报告他们的时间和大小
package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	start := time.Now()
	ch := make(chan string)
	filename := os.Args[1]
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "fetchall_2:%v \n", err)
	}

	l_ := strings.Split(string(data), "\n")
	length_ := len(l_)

	for _, line := range l_ {
		go fetch(line, ch)
	}
	for i := 0; i < length_; i++ {
		fmt.Println(<-ch)
	}
	fmt.Printf("%.3fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}

	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close()
	if err != nil {
		ch <- fmt.Sprintf("While reading %s: %v", url, err)
		return
	}

	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.3fs %7d %s", secs, nbytes, url)
}
