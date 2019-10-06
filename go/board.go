// Filename: board.go
// coding:utf-8
// read serial 
package main

import (
	"log"
	"github.com/tarm/serial"
)

func main () {
	c := &serial.Config{Name:"/dev/ttyUSB0", Baud: 9600}
	s, err := serial.OpenPort(c)
	if err != nil {
		log.Fatal(err)
	}

	buf := make([]byte, 128)
	n, err := s.Read(buf)
	if err != nil {
		log.Fatal(err)
	}
	log.Print("%q", buf[:n])
}
