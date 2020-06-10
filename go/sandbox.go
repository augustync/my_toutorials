package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Welcome to the playground!")

	fmt.Println("The time is", time.Now())

	// my own things to do

	var d = time.Now() // that didnt worked well
	println("test1")
	fmt.Println(d)

	// from the documentation example
	start := time.Now()
	sum := 0
	for x := 0; x < 10; x++ {
		sum++
		time.Sleep(10 * time.Second)
	}
	println("sum is: ", sum)
	t := time.Now()
	elapsed := t.Sub(start)

	println("took it : ", elapsed.Minutes)
}
