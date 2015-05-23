package main

import "fmt"

const N = 100
func main() {
	sqr_sum := N * (N + 1) / 2
	sqr_sum *= sqr_sum
	var sum_sqr = 0
	for i:=1; i <= 100; i++ {
		sum_sqr += i * i
	}
	fmt.Println(sqr_sum - sum_sqr)
}