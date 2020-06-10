/*
Functions
A function can take zero or more arguments.
In this example, add takes two parameters of type int.
Notice that the type comes after the variable name.
(For more about why types look the way they do, see the article on Go's declaration syntax.)
https://blog.golang.org/declaration-syntax

Functions continued
When two or more consecutive named function parameters share a type, you can omit the type from all but the last.
In this example, we shortened
x int, y int
to
x, y int
*/

package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

// my own functions
func remove(x int, y int) int {
	return x - y
}

func divide(x int, y int) int {
	return x / y
}

func multiplay(x, y int) int {
	return x * y
}

func add2(x, y int) int {
	return x + y
}

//func test(y, x int) float32 {
//	return (float32) x * y
//}

func main() {
	fmt.Println(add(42, 13))
	println(remove(5, 2))
	println(divide(6, 2))
	println(divide(5, 2))
	println(multiplay(3, 4))
	fmt.Println(add2(42, 13))
	//println(test(3, 4))
}
